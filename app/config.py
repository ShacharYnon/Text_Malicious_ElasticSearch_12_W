import os



CONNECTION_ADDRESS_ES = os.getenv("CONNECTION_ADDRESS_ES" ,"http://localhost:9200")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# CSV_FILE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "tweets_injected_3.csv"))
CSV_FILE_PATH = os.path.join(BASE_DIR, "data", "tweets_injected_3.csv")
INDEX_GROUPS = os.getenv("INDEX_GROUPS" ,"tweets")
ES_MAPPING = {
                "mappings": {
                    "properties": {
                        "TweetID": {"type": "Keyword"},
                        "CreateDate": {"type": "Keyword"},
                        "Antisemitic": {"type": "boolean"},
                        "text": {"type": "text"}
                                }
                        }
                }


