from .converting import Convert
from .. import config
from elasticsearch import Elasticsearch ,helpers
import logging 
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

class Processing:

    def __init__(self):
        self.es = None
        self.data = Convert().convert_csv_to_dict()
        self.index_name = config.INDEX_GROUPS
        self.mapping = config.ES_MAPPING
        self.query = {"query": {"match_all": {}}}

    def connection_to_es(self ,address):
        try:
            self.es = Elasticsearch(address)
            logger.info("Connection to ES successful")
            return self.es
        except Exception as e:
            logger.info(f"ERROR: from Processing.connection_to_es: {e}")

    def es_mapping(self):
        try:
            if not self.es.indices.exists(index= self.index_name):
                self.es.indices.create(index= self.index_name ,body=self.mapping)
                logger.info(f"The index was successful.")
                results = helpers.scan(self.es,index=self.index_name, body=self.query)
                return results
        except Exception as e:
            logger.info(f"ERROR: From Processing.indexing: {e}")

    def es_indexing(self ,index_name ,data):
        try:
            actions = [{"_index": index_name, "_source": doc} for doc in data]
            helpers.bulk(client=self.connection_to_es, actions=actions)
            logging.info(f"Successfully indexed documents")
        except Exception as e:
            logging.error(f"Failed to index data: {e}")
            raise(e)

    

if __name__ == "__main__":
    es = Processing()
    es.connection_to_es(config.CONNECTION_ADDRESS_ES)
    e = es.es_indexing()
    print(e)
    
