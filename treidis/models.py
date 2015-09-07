#!/usr/bin/python
# coding: utf-8

class orderModel(object):

    amount = None
    price = None
    traderid = None

    def __init__(self, order):
        self.price = order[0]
        self.amount = order[1]
        self.traderid = order[2]

    def __repr__(self):
        return "OrderModel amount: %f, price: %f, trader: %d" % (self.amount, self.price, self.traderid)

    def __str__(self):
        return "OrderModel amount: %f, price: %f, trader: %d" % (self.amount, self.price, self.traderid)

class FoxBitOrderbookModel(object):
    # bids = compra, asks = venda
    bids = []
    asks = []

    # Entrada: orderbook (json ou dict)
    def __init__(self, orderbook, fee):
        for order in orderbook.get('bids'):
            self.bids.append(orderModel(order))
        for order in orderbook.get('asks'):
            self.asks.append(orderModel(order))
        self.fee = fee

    def getBestBid(self):
        return self.bids[0]

    def getBestAsk(self):
        return self.asks[0]

    def getSpread(self):
        return self.asks[0].price - self.bids[0].price

    def __getPriceFor(self, amount, orders):
        total = 0
        liquido = 0
        price = 0
        for order in orders:
            total += order.amount
            if(total < amount):
                liquido += order.amount - (order.amount * self.fee)
                price += (order.price * order.amount)
            else:
                price += (order.price * (order.amount - (total - amount)))
                liquido += (order.amount - (total - amount)) - ((order.amount - (total - amount)) * self.fee)
                # Confere se resta btc para comprar e compensar a taxa do total
                if(total - amount >= ((amount - liquido) + ((amount - liquido) * self.fee))):
                    price += (order.price * ((amount - liquido) + ((amount - liquido) * self.fee)))
                    liquido += (amount - liquido)
                else:
                    continue
                total -= total - amount
                break
        print ''
        print "Total: %f Liquido: %f" % (total, liquido)
        return price

    def getBidPriceFor(self, amount):
        return self.__getPriceFor(amount, self.bids)

    def getAskPriceFor(self, amount):
        return self.__getPriceFor(amount, self.asks)

    def getSpreadFor(self, amount):
        return self.getAskPriceFor(amount) - self.getBidPriceFor(amount)

if __name__ == "__main__":
    json = {u'pair': u'BTCBRL', u'bids': [[950.0, 0.4, 90802712], [900.0, 0.4, 90800427], [800.0, 0.4, 90804599], [750.0, 1, 90804599]], u'asks': [[1000.0, 0.4, 90802712], [1005.0, 0.4, 90800427], [1010.0, 0.4, 90804599], [1015.0, 0.4, 90800427]]}
    orderb = FoxBitOrderbookModel(json, 0.0025)
    print 'Best bid: %s' % orderb.getBestBid()
    print 'Best ask: %s' % orderb.getBestAsk()
    print 'Spread: %s' % orderb.getSpread()
    print 'Bid price for 1 BTC: %f' % orderb.getBidPriceFor(1)
    print 'Bid price for 2 BTC: %f' % orderb.getBidPriceFor(2)
    print 'Bid price for 0.4 BTC: %f' % orderb.getBidPriceFor(0.4)
    print 'Bid price for 0.6 BTC: %f' % orderb.getBidPriceFor(0.6)
    print 'Bid price for 0.8 BTC: %f' % orderb.getBidPriceFor(0.8)
    print 'Bid price for 1.2 BTC: %f' % orderb.getBidPriceFor(1.2)
    print 'Ask price for 1 BTC: %f' % orderb.getAskPriceFor(1)
    print 'Spread for 1 BTC: %f' % orderb.getSpreadFor(1)
