#!/usr/bin/python
# coding: utf-8

class bidModel(object):

    amount = None
    price = None
    total = None

    def __init__(self, bid):
        self.price = bid[0]
        self.amount = bid[1]
        self.total = bid[2]

    def __repr__(self):
        return "bid amount: %2.f,"

    def __str__(self):
        return "member of Test"

class FoxBitOrderbookModel(object):
    bids = []
    asks = []

    def load(self, bids, asks):
        pass

    def parseJSON(self, json):
        bids = json.get('bids')
        for bid in bids:
            bid.pop(2)
            bid.append(bid[0] * bid[1])
            self.bids.append(bidModel(bid))

        asks = json.get('asks')
        for ask in asks:
            ask.pop(2)
            ask.append(ask[0] * ask[1])
            self.asks.append(askModel(ask))
