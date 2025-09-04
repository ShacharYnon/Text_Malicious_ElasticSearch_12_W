import csv
from .. import config
import logging
logger = logging.getLogger(__name__)

class Convert:

    def __init__(self ,path:str):
        self.path = path
        self.data = None


    def convert_csv_to_dict(self ,path = None):
        if path is None:
            path = self.path
        
        try:
            with open(path ,encoding="utf-8") as f:
                reader = csv.DictReader(f)
                self.data = list(reader)
                logger.info("Converting CSV file successfully completed")
                return self.data
        except Exception as e:
            logger.error(f" ERROR: From convert_csv_to_es: {e}")



if __name__ == "__main__":
    con = Convert(config.CSV_FILE_PATH)
    row = con.convert_csv_to_dict()
    print(type(row))
    for r in row:
        print(type(r))


# python -m app.es.connection_and_converting