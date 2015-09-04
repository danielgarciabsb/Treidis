# coding: utf-8

# Import lib
import importlib

# Arquivo de configuracoes
import ConfigParser

# Threads
import threading

# Tempo
import time

# Testes
import unittest
import tests

# JSON
import json

# Sinais
import signal

# Sistema
import sys

# Log
from log import logging

# Requisicoes API
from apirequests import APIRequests

def signal_handler(signal, frame):
    logger = logging.getLogger('treidis')
    logger.info('Finalizando sistema Treidis... Signal: %s' % signal)
    logger.info('Sistema Treidis finalizado.')
    logging.shutdown()
    sys.exit(0)

class Treidis(object):

    # Nome do arquivo de configuracao
    config_filename = 'treidis/config/treidis.conf'

    # Inicializa log da aplicacao principal
    logger = logging.getLogger('treidis')

    def __init__(self):
        # Inicializa hooks de sinais de finalizacao
        signal.signal(signal.SIGINT, signal_handler)
        signal.signal(signal.SIGTERM, signal_handler)
        signal.signal(signal.SIGQUIT, signal_handler)
        signal.signal(signal.SIGABRT, signal_handler)

        # Inicializa testes e verifica se todos foram validados com sucesso
        test = unittest.TextTestRunner(verbosity=2, failfast=True).run(
                    unittest.TestLoader().loadTestsFromModule(tests))
        if not test.wasSuccessful():
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

        while True:
            time.sleep(1)

    def __loadAlgos(self):
        for algo in self.algolist:
            try:
                globals()[algo] = importlib.import_module('algoritmos.' + algo)
            except (ImportError, Exception) as e:
                self.logger.error('Falha ao importar algoritmo: %s' % e)
                exit()
        for algo in self.algolist:
            self.logger.info('Iniciando algoritmo: %s' % algo)
            log = logging.getLogger('treidis.' + algo)
            worker = threading.Thread(name=str(algo), target=eval(algo + '.' + algo), args=[self.apirequests, log])
            worker.setDaemon(True)
            worker.start()


if __name__ == "__main__":
    treidis = Treidis()
