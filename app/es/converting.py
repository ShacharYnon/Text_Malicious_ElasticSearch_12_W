from elasticsearch import Elasticsearch
import csv
from .. import config


class Convert:

    def __init__(self):
        self.es = Elasticsearch(config.CONNECTION_ADDRESS_ES)
        self.data = None



    def convert_csv_to_es(self):
        try:
            with open(config.CSV_FILE_PATH ,encoding="utf-8") as f:
                reader = csv.DictReader(f)
                self.data = list(reader)
                print("Converting CSV file successfully completed")
                return self.data
        except Exception as e:
            print(f" ERROR: From convert_csv_to_es: {e}")



if __name__ == "__main__":
    es = Convert()
    row = es.convert_csv_to_es()
    for r in row:
        print(r)