from enum import Enum


class CryptoPairs(Enum):
    usd = 'btcusd'
    eth = 'ethusd'
    ltc = 'ltcusd'
    sol = 'solusd'
    ada = 'adausd'
    avax = 'avaxusd'
    dot = 'dotusd'
    luna = 'lunausd'
    grt = 'grtusd'
    xrp = 'xrpusd'
    doge = 'dogeusd'
    matic = 'maticusd'
    link = 'linkusd'
    shib = 'shibusd'
    audio = 'audiousd'


class CryptoExchanges(Enum):
    kraken = 'kraken'
    binance_us = 'binance-us'
    binance = 'binance'
    coin = 'coinbase-pro'
    ftx = 'ftx'


