#!/usr/bin/python
# coding: utf-8

# Arquivo de configuracoes
import ConfigParser

# Threads
import threading

# Tempo
import time

# Requisicoes API
from apirequests import APIRequests

# Helpers
from helper import floatToExc

# Log
from log import logging

# Testes
import unittest
import treidistests

import json

from algoritmos import *

class Treidis(object):

    config_filename = 'treidis.conf'
    logger = logging.getLogger('treidis')

    def __init__(self):
        tests = unittest.TextTestRunner(verbosity=2, failfast=True).run(
                    unittest.TestLoader().loadTestsFromModule(treidistests))
        if not tests.wasSuccessful():
            exit()

        # Carrega configuracoes
        self.options = ConfigParser.ConfigParser()
        self.options.read(self.config_filename)

        # Obtem a lista de algoritmos da configuacao
        self.algolist = json.loads(self.options.get("SYSTEM","algoritmos"))

        # Instancia o modulo APIRequests
        self.apirequests = APIRequests(self.options)
        self.__loadAlgos()

        self.logger.info('Sistema Treidis iniciado.')

    def __loadAlgos(self):
        oportunista()
        #for algo in self.algolist:
        #    threading.Thread(name=str(algo), target=eval(algo)).start()


if __name__ == "__main__":
    treidis = Treidis()
    #print treidis.apirequests.getBalance()
    #fox = APIRequests(treidis.options)
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
    #print fox.buyBitcoins(10101010, 1234567890)
    #print fox.buyBitcoins(floatToExc(1.5), floatToExc(random.uniform(10, 100)))
    #print fox.buyBitcoins(123456, floatToExc(101.161))
    #print fox.getBTCDepositAddress(random.randint(1, 100))
    #print dict(treidis.config.items('API'))
