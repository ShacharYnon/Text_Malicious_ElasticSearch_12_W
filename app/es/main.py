from .. import config
from .converting import Convert
from . loading import Processing
from .processing import SentimentEnhancer
from elasticsearch import Elasticsearch ,helpers
import logging


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)


class manager_ES:
    def __init__(self):
        self.es = None
        self.data = None
        self.index_name = config.INDEX_GROUPS

    def run(self):
        try:
            # Step 1: Connect to Elasticsearch
            self.processor = Processing()
            self.processor.connection_to_es(config.CONNECTION_ADDRESS_ES)

            # Step 2: Convert CSV to dictionary
            self.data = Convert(config.CSV_FILE_PATH).convert_csv_to_dict()

            if not self.data:
                logger.error("No data to process after conversion.")
                return
            print(type(self.data))

            # Step 3: Enrich data with sentiment analysis
            self.data = SentimentEnhancer().enrich_documents(self.data)

            if not self.data:
                logger.error("No data to process after enrichment.")
                return

            # Step 4: Create index and mapping in Elasticsearch
            self.processor.es_mapping()

            # Step 5: Index enriched data into Elasticsearch
            indexed_count = self.processor.es_indexing(self.index_name, self.data)
            logger.info(f"Indexed {indexed_count} documents into {self.index_name}")

        except Exception as e:
            logger.error(f"Error in manager_ES.run: {e}")
            raise





if __name__ == "__main__":
    manager = manager_ES()
    manager.run()   