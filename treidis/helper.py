#!/usr/bin/python
# coding: utf-8

from __future__ import division

# Recebe um float ex: 45.96 e retorna o valor para enviar a exchange
def floatToExc(money):
    return int(money * 100000000)

# Recebe um inteiro ex: 4596000000 e retorna float 45.96
def excToFloat(money):
    return float(money / 100000000)

def valor(quantity, price):
    return quantity * price

if __name__ == "__main__":
    print 'Valor 20000000 sats ao preco 100.0 = ' + str(valor(excToFloat(20000000), 100.0)) + ' reais'
    print '20000000 sats = ' + str(excToFloat(20000000)) + ' btc'
