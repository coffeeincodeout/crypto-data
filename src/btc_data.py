from src.api_request.api_request import ApiRequest
from src.database_class.postgres_db import PostgresDataBase
from src.database_class.databaseconn import PostgresqlConn
from enum import Enum
import csv
import os
import datetime


class BTCPairs(Enum):
    usd = 'btcusd'
    eur = 'btceur'
    gbp = 'btcgbp'


def timestamp_format(timestamp: int) -> datetime:
    return datetime.datetime.fromtimestamp(timestamp).strftime('%m/%d/%Y')


def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def main():
    path = os.getcwd()
    period = 86400
    after = 11580533200
    before = 1609477200

    for pair in BTCPairs:
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
        file_path = path + '/crypto_files/{}.csv'.format(pair.value)
        with open(file_path, 'w', newline='') as btc_data:
            writer = csv.writer(btc_data)
            # add columns to the csv file
            writer.writerow(cols)
            for row in data:
                # cast timestamp to date
                row[0] = timestamp_format(row[0])
                # append the asset type to the row
                row.append(pair.value)
                # write the row to csv file
                writer.writerow(row)
    # this section will get the csv files and upload them to the database
    csv_file_path = path + '/crypto_files'
    for file in os.listdir(csv_file_path):
        file = csv_file_path + '/' + file
        with open(file, 'r') as btc_csv_file:
            reader = csv.reader(btc_csv_file)
            header = next(reader)

            for row in reader:
                data_base = PostgresDataBase(
                    dbname='bitcoin_data',
                    username=os.getenv('USER'),
                    password=os.getenv('PASSWORD'),
                    hostname=PostgresqlConn.hostname.value,
                    port=PostgresqlConn.port.value
                )
                data_base.conn_db()
                data_base.create(
                    table='bitcoin_price',
                    columns=header,
                    data=row
                )
                data_base.close_db_conn()
    print("Data inserted into table")


if __name__=='__main__':
    main()

