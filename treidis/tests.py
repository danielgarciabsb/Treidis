# coding: utf-8

import unittest
import os.path

import ConfigParser

class ConfigFileTest(unittest.TestCase):

    config_filename = 'treidis/config/treidis.conf'

    def setUp(self):
        if not os.path.isfile(self.config_filename):
            raise Exception('APIRequests __loadConfig: config file %s not found.' % self.config_filename)
        self.options = ConfigParser.ConfigParser()
        self.options.read(self.config_filename)

    def testHasLog(self):
        if not self.options.has_option('SYSTEM','log'):
            raise Exception('ConfigFileTest testHasLog: [SYSTEM] option "log" not found.')
        self.options.getboolean('SYSTEM','log')

    def testHasAuthKey(self):
        if not self.options.has_option('AUTH','key'):
            raise Exception('ConfigFileTest testHasAuthKey: [AUTH] option "key" not found.')

    def testHasSecretKey(self):
        if not self.options.has_option('AUTH','secret'):
            raise Exception('ConfigFileTest testHasSecretKey: [AUTH] option "secret" not found.')

    def testHasMaxTries(self):
        if not self.options.has_option('API','max_tries'):
            raise Exception('ConfigFileTest testHasMaxTries: [API] option "max_tries" not found.')
        self.options.getint('API','max_tries')

    def testHasTimeout(self):
        if not self.options.has_option('API','timeout'):
            raise Exception('ConfigFileTest testHasTimeout: [API] option "timeout" not found.')
        self.options.getint('API','timeout')

    def testHasSslVerify(self):
        if not self.options.has_option('API','ssl_verify'):
            raise Exception('ConfigFileTest testHasSslVerify: [API] option "ssl_verify" not found.')
        self.options.getboolean('API','ssl_verify')

    def testHasFoxBitApi(self):
        if not self.options.has_option('API','foxbit_api'):
            raise Exception('ConfigFileTest testHasFoxBitApi: [API] option "foxbit_api" not found.')

    def testHasFoxBitOrderbook(self):
        if not self.options.has_option('API','foxbit_orderbook'):
            raise Exception('ConfigFileTest testHasFoxBitOrderbook: [API] option "foxbit_orderbook" not found.')

    def testHasFoxBitTicker(self):
        if not self.options.has_option('API','foxbit_ticker'):
            raise Exception('ConfigFileTest testHasFoxBitTicker: [API] option "foxbit_ticker" not found.')

    def testHasBitfinexTicker(self):
        if not self.options.has_option('API','bitfinex_ticker'):
            raise Exception('ConfigFileTest testHasBitfinexTicker: [API] option "bitfinex_ticker" not found.')

    def testHasBitstampTicker(self):
        if not self.options.has_option('API','bitstamp_ticker'):
            raise Exception('ConfigFileTest testHasBitstampTicker: [API] option "bitstamp_ticker" not found.')

    def testHasOkcoinTicker(self):
        if not self.options.has_option('API','okcoin_ticker'):
            raise Exception('ConfigFileTest testHasOkcoinTicker: [API] option "okcoin_ticker" not found.')

    def testHasBtceTicker(self):
        if not self.options.has_option('API','btce_ticker'):
            raise Exception('ConfigFileTest testHasBtceTicker: [API] option "btce_ticker" not found.')

class FoxBitOrderbookModelTest(unittest.TestCase):
    pass
