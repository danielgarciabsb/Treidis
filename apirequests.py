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

    def requestAPI(self, url):
        try:
            data = requests.get(url, verify=False, timeout=0.001).json()
        except requests.exceptions.ConnectionError, e:
            self.logger.error('ConnectionError: %s' % e)
        except requests.exceptions.Timeout, e:
            self.logger.error('Timeout: %s' % e)

    def getFoxBitOrderbook(self):
        data = self.requestAPI(self.FOXBIT_ORDERBOOK)
        return data

fox = APIRequests()
fox.getFoxBitOrderbook()
