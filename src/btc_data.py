from src.api_request.api_request import ApiRequest
from src.database_class.postgres_db import PostgresDataBase
from src.database_class.databaseconn import PostgresqlConn
from src.crypto.cryptodata import CryptoPairs
from datetime import datetime
from enum import Enum
import csv
import os
import time


class BTCPairs(Enum):
    usd = 'btcusd'
    eur = 'btceur'
    gbp = 'btcgbp'


def timestamp_format(timestamp: int) -> str:
    return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')


def convert_date_to_timestamp(date: str) -> str:
    d = datetime.strptime(date, '%Y-%m-%d')
    ts = datetime.timestamp(d)
    if isinstance(ts, float):
        return str(ts).split('.')[0]
    return str(ts)


def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def main():
    period = '86400'
    after = convert_date_to_timestamp('2020-01-01')
    before = convert_date_to_timestamp('2022-04-04')
    # loop through each bitcoin pair in BTCPairs
    for pair in CryptoPairs:
        crypto_watch_base_url = 'https://api.cryptowat.ch/'
        end_point = 'markets/kraken/{0}/ohlc?period={1}&after={2}&before={3}'.format(
            pair.value, period, after, before)
        crypto_watch_data = ApiRequest(
            base_url=crypto_watch_base_url,
            end_point=end_point,
            request_method='GET'
        )

        crypto_watch_data()
        # get the json response for daily prices
        data = crypto_watch_data.data_response()['result']['86400']
        # hard coded headers to add to csv file
        cols = ["closetime", "openprice", "highprice", "lowprice", "closeprice", "volume", "quotevolume", "asset"]
        # this is the file path to store the csv file
        for row in data:
            # cast timestamp to date
            row[0] = timestamp_format(row[0])
            # append pair to the asset row
            row.append(pair.value)
            # connect to database
            data_base = PostgresDataBase(
                dbname='bitcoin_data',
                username='postgres',
                password='admin1234',
                hostname=PostgresqlConn.hostname.value,
                port=PostgresqlConn.port.value
            )
            data_base.conn_db()
            # add row to database
            data_base.create(
                table='crypto_test',
                columns=cols,
                data=row
            )
            # close database connection
            data_base.close_db_conn()

    print("Data inserted into table")


if __name__=='__main__':
    main()

