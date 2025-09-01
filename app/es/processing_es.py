from .converting import Convert
from .. import config
from elasticsearch import Elasticsearch

class Processing:

    def __init__(self):
        self.es = Elasticsearch(config.CONNECTION_ADDRESS_ES)
        self.data = Convert().convert_csv_to_dict()

    def mapping(self):
        pass

    def indexing(self):
        pass

