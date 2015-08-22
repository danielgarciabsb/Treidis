#!/usr/bin/python
# coding: utf-8

import requests
from requests import Request, Session

from log import logging

class APIRequests(object):

    # Livro de ofertas da FoxBit
    FOXBIT_ORDERBOOK = 'https://api.blinktrade.com/api/v1/BRL/orderbook'

    # Trades da FoxBit
    FOXBIT_TRADES = 'https://api.blinktrade.com/api/v1/BRL/trades'

    # Ticker da FoxBit
    FOXBIT_TICKER = 'https://api.blinktrade.com/api/v1/BRL/ticker'

    # Ticker da Bitfinex
    BITFINEX_TICKER = 'https://api.bitfinex.com/v1/pubticker/BTCUSD'

    # Ticker da Bitstamp
    BITSTAMP_TICKER = 'https://www.bitstamp.net/api/ticker/'

    # Ticker da OKCoin
    OKCOIN_TICKER = 'https://www.okcoin.com/api/v1/ticker.do?symbol=btc_usd'

    # Ticker da BTC-e
    BTCE_TICKER = 'https://btc-e.com/api/3/ticker/btc_usd'

    logger = logging.getLogger('treidis.apirequests')

    def __init__(self):
        pass

    def __requestAPI(self, url, timeout):
        try:
            data = requests.get(url, verify=False, timeout=timeout)
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

    def __makeRequest(self, api, timeout=5):
        try:
            data = self.__requestAPI(api, timeout)
        except Exception, e:
            self.logger.error('Falha ao obter reposta da API: %s' % api)
        else:
            self.logger.info('API obtida com sucesso: %s' % api)
            return data

    def getFoxBitOrderbook(self):
        return self.__makeRequest(self.FOXBIT_ORDERBOOK, 10)

    def getFoxBitTrades(self):
        return self.__makeRequest(self.FOXBIT_TRADES)

    def getFoxBitTicker(self):
        return self.__makeRequest(self.FOXBIT_TICKER)

    def getBitfinexTicker(self):
        return self.__makeRequest(self.BITFINEX_TICKER)

    def getBitstampTicker(self):
        return self.__makeRequest(self.BITSTAMP_TICKER)

    def getOKCoinTicker(self):
        return self.__makeRequest(self.OKCOIN_TICKER)

    def getBTCeTicker(self):
        return self.__makeRequest(self.BTCE_TICKER)

fox = APIRequests()
print fox.getFoxBitOrderbook().json()
print fox.getFoxBitTrades().json()
print fox.getFoxBitTicker().json()
print fox.getBitfinexTicker().json()
print fox.getBitstampTicker().json()
print fox.getOKCoinTicker().json()
print fox.getBTCeTicker().json()
