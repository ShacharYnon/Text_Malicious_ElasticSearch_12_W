import csv
from .. import config


class Convert:

    def __init__(self):
        
        self.data = None



    def convert_csv_to_dict(self):
        try:
            with open(config.CSV_FILE_PATH ,encoding="utf-8") as f:
                reader = csv.DictReader(f)
                self.data = list(reader)
                print("Converting CSV file successfully completed")
                return self.data
        except Exception as e:
            print(f" ERROR: From convert_csv_to_es: {e}")



if __name__ == "__main__":
    con = Convert()
    row = con.convert_csv_to_dict()
    for r in row:
        print(r)


# python -m app.es.connection_and_converting