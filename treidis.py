#!/usr/bin/python
# coding: utf-8

import ConfigParser
from apirequests import APIRequests
import random
from helper import real

class Treidis(object):

    def __init__(self):
        self.loadConfig()

    def loadConfig(self):
        self.config = ConfigParser.ConfigParser()
        self.config.read('treidis.conf')

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
    print fox.createOrder('1', 10101010, 1234567890)
    print fox.createOrder('1', 666999, real(45.96))
    print fox.createOrder('1', 123456, real(101.161))
    #print fox.getBTCDepositAddress(random.randint(1, 100))
    #print dict(treidis.config.items('API'))
