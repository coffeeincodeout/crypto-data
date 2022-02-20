from enum import Enum


class BTCPairs(Enum):
    usd = 'btcusd'
    eur = 'btceur'
    gbp = 'btcgbp'


class CryptoExchanges(Enum):
    krak = 'kraken'
    binance = 'binance'
    coin = 'coinbase'


