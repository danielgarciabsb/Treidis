#!/usr/bin/python
# coding: utf-8

import ConfigParser
import threading
import time
import os.path

from apirequests import APIRequests
from helper import floatToExc
from log import logging

import random

class Treidis(object):

    config_filename = 'treidis.conf'

    def __init__(self):
        self.__loadConfig()
        self.apirequests = APIRequests(self.options)

    def __loadConfig(self):
        self.options = ConfigParser.ConfigParser()
        try:
            if not os.path.isfile(self.config_filename):
                raise Exception('APIRequests __loadConfig: config file %s not found.' % self.config_filename)

            self.options.read(self.config_filename)

            if not self.options.has_section('AUTH') or not self.options.has_section('SYSTEM') or not self.options.has_section('API'):
                raise Exception('APIRequests __loadConfig: some config file sections not found.')

            if not options.has_option('AUTH','key'):
                raise Exception('APIRequests __init__: [AUTH] option "key" not found.')

            if not options.has_option('AUTH','key'):
                raise Exception('APIRequests __init__: [AUTH] option "key" not found.')

        except Exception, e:
            logging.error('Treidis __loadConfig: %s' % e)
            exit(1)

if __name__ == "__main__":
    treidis = Treidis()

    fox = APIRequests(treidis.config)

    #print fox.getFoxBitOrderbook()
    #print fox.getFoxBitTrades()
    #print fox.getFoxBitTicker()
    #print fox.getBitfinexTicker()
    #print fox.getBitstampTicker()
    #print fox.getOKCoinTicker()
    #print fox.getBTCeTicker()
    #print fox.getBalance()
    #print fox.getOpenOrders()
    #print fox.createOrder('1', random.randint(10000, 100000), random.randint(100000000, 1000000000))
    print fox.buyBitcoins(10101010, 1234567890)
    print fox.buyBitcoins(floatToExc(1.5), floatToExc(random.uniform(10, 100)))
    print fox.buyBitcoins(123456, floatToExc(101.161))
    #print fox.getBTCDepositAddress(random.randint(1, 100))
    #print dict(treidis.config.items('API'))
