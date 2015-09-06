class Oportunista(object):

    def __init__(self, investimento_maximo, taxa, api, log):
        self.investimento_maximo = investimento_maximo
        self.taxa = taxa

    

def oportunista(api, log):
    log.info('Iniciando algoritmo Oportunista')
    oportunista = Oportunista(100.0, 0.0025, api, log)
    log.info('Algoritmo Oportunista finalizado')
