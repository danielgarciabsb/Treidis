#!/usr/bin/python
# coding: utf-8

import requests
import hashlib
import hmac
import time
import json
import datetime

from log import logging

class APIRequests(object):

    # Logger do modulo
    logger = logging.getLogger('treidis.apirequests')

    def __init__(self, options=None):
        if not options:
            raise Exception('APIRequests __init__: options not defined')
        else:
            # Chave do usuario
            self.key = options.get('AUTH','key')
            # Chave de segredo
            self.secret = options.get('AUTH','secret')
            # Maximo tentativas
            self.max_tries = options.getint('API','max_tries')
            # Tempo maximo de espera para requisicoes
            self.timeout = options.getint('API','timeout')
            # Verificar certificados SSL
            self.ssl_verify = options.getboolean('API','ssl_verify')
            # API Rest da FoxBit
            self.foxbit_api = options.get('API','foxbit_api')
            # Livro de ofertas da FoxBit
            self.foxbit_orderbook = options.get('API','foxbit_orderbook')
            # Trades da FoxBit
            self.foxbit_trades = options.get('API','foxbit_trades')
            # Ticker da FoxBit
            self.foxbit_ticker = options.get('API','foxbit_ticker')
            # Ticker da Bitfinex
            self.bitfinex_ticker = options.get('API','bitfinex_ticker')
            # Ticker da Bitstamp
            self.bitstamp_ticker = options.get('API','bitstamp_ticker')
            # Ticker da OKCoin
            self.okcoin_ticker = options.get('API','okcoin_ticker')
            # Ticker da BTC-e
            self.btce_ticker = options.get('API','btce_ticker')

    def __requestAPI(self, url, headers=None, payload=None):
        try:
            if not payload:
                data = requests.get(url, verify=self.ssl_verify, timeout=self.timeout, headers=headers)
            else:
                data = requests.post(url, verify=self.ssl_verify, timeout=self.timeout,
                                    headers=headers, json=payload)
            data.raise_for_status()
        except requests.exceptions.RequestException, e:
            self.logger.error('RequestException: %s' % e)
            raise
        except requests.exceptions.ConnectionError, e:
            self.logger.error('ConnectionError: %s' % e)
            raise
        except requests.exceptions.HTTPError, e:
            self.logger.error('HTTPError: %s' % e)
            raise
        except requests.exceptions.URLRequired, e:
            self.logger.error('URLRequired: %s' % e)
            raise
        except requests.exceptions.TooManyRedirects, e:
            self.logger.error('TooManyRedirects: %s' % e)
            raise
        except requests.exceptions.Timeout, e:
            self.logger.error('Timeout: %s' % e)
            raise
        else:
            return data

    def __makeRequest(self, api, headers=None, payload=None):
        for tries in range(0, self.max_tries):
            try:
                self.logger.info('Tentativa %d de obter a API: %s' % (tries + 1,api))
                data = self.__requestAPI(api, headers, payload).json()
            except Exception, e:
                self.logger.error('Falha ao obter reposta da API: %s' % api)
                if(tries < self.max_tries - 1):
                    self.logger.warn('Tentando obter API novamente...')
                elif(tries == self.max_tries - 1):
                    self.logger.error('ERRO FATAL: Falha ao obter reposta da API: %s após %d tentativas!'
                        % (api, self.max_tries))
            else:
                self.logger.info('API obtida com sucesso: %s' % api)
                return data

    def __generateNonce(self):
        dt = datetime.datetime.now()
        return str(int((time.mktime( dt.timetuple() )  + dt.microsecond/1000000.0) * 1000000))

    def __makeSignature(self, nonce=None):
        if not nonce:
            raise Exception('APIRequests __makeSignature: Nonce required.')
        else:
            return hmac.new(self.secret, nonce, digestmod=hashlib.sha256).hexdigest()

    def __makeHeaders(self):
        nonce = self.__generateNonce()
        signature = self.__makeSignature(nonce)
        return {'user-agent': 'treidis/0.0.1',
            'Content-Type':'application/json',
            'APIKey': self.key,
            'Nonce': nonce,
            'Signature': signature,
            }

    # Todos retornos sao em JSON
    def getFoxBitOrderbook(self):
        return self.__makeRequest(self.foxbit_orderbook)

    def getFoxBitTrades(self):
        return self.__makeRequest(self.foxbit_trades)

    def getFoxBitTicker(self):
        return self.__makeRequest(self.foxbit_ticker)

    def getBitfinexTicker(self):
        return self.__makeRequest(self.bitfinex_ticker)

    def getBitstampTicker(self):
        return self.__makeRequest(self.bitstamp_ticker)

    def getOKCoinTicker(self):
        return self.__makeRequest(self.okcoin_ticker)

    def getBTCeTicker(self):
        return self.__makeRequest(self.btce_ticker)

    def getBalance(self):
        payload = {
            "MsgType": "U2",
            "BalanceReqID": 1
        }
        return self.__makeRequest(self.foxbit_api, self.__makeHeaders(), payload)

    def getOpenOrders(self):
        payload = {
            "MsgType": "U4",
            "OrdersReqID": 1,
            "Page": 0,
            "PageSize": 100,
            # Set it to "has_leaves_qty eq 1" to get open orders, "has_cum_qty eq 1" to get executed orders, "has_cxl_qty eq 1" to get cancelled orders
            "Filter":["has_leaves_qty eq 1"],
        }
        return self.__makeRequest(self.foxbit_api, self.__makeHeaders(), payload)

    def createOrder(self, side, quantity, price):
        payload = {
            "MsgType":"D",              # New Order Single message. Check for a full doc here: http://www.onixs.biz/fix-dictionary/4.4/msgType_D_68.html
            "ClOrdID": str(int(time.time())), # Unique identifier for Order as assigned by you
            "Symbol":"BTCBRL",          # Can be BTCBRL, BTCPKR, BTCVND, BTCVEF, BTCCLP.
            "Side": side,                 # 1 - Buy, 2-Sell
            "OrdType":"2",              # 2 - Limited order
            "OrderQty": quantity,         # Qty in saothis
            "Price": price,        # Price in satoshis
            "BrokerID":4                # 1=SurBitcoin, 3=VBTC, 4=FoxBit, 5=Tests , 8=UrduBit, 9=ChileBit
        }
        return self.__makeRequest(self.foxbit_api, self.__makeHeaders(), payload)

    def getBTCDepositAddress(self, reqid):
        payload = {
            "MsgType":"U18",    # Deposit request
            "DepositReqID": reqid,   # Deposit Request ID.
            "Currency":"BTC",   # Currency.
            "BrokerID": 4       # Exchange ID
        }
        return self.__makeRequest(self.foxbit_api, self.__makeHeaders(), payload)
