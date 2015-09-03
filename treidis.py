#!/usr/bin/python
# coding: utf-8

# Arquivo de configuracoes
import ConfigParser

# Threads
import threading

# Requisicoes API
from apirequests import APIRequests

# Log
from log import logging

# Testes
import unittest
import treidistests

import json

import importlib

class Treidis(object):

    # Nome do arquivo de configuracao
    config_filename = 'treidis.conf'

    # Inicializa log da aplicacao principal
    logger = logging.getLogger('treidis')

    def __init__(self):
        # Inicializa testes e verifica se todos foram validados com sucesso
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

        # Indica que o sitema iniciou
        self.logger.info('Sistema Treidis iniciado.')

        # Inicializa algoritmos
        self.__loadAlgos()

    def __loadAlgos(self):
        for algo in self.algolist:
            try:
                globals()[algo] = importlib.import_module('algoritmos.' + algo)
            except (ImportError, Exception) as e:
                self.logger.error('Falha ao importar algoritmo: %s' % e)
                exit()
        for algo in self.algolist:
            self.logger.info('Iniciando algoritmo: %s' % algo)
            threading.Thread(name=str(algo), target=eval(algo + '.' + algo)).start()


if __name__ == "__main__":
    treidis = Treidis()
