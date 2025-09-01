import os

CONNECTION_ADDRESS_ES = os.getenv("CONNECTION_ADDRESS_ES" ,"http://localhost:9200")

# BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(_file_), "..",".."))
CSV_FILE_PATH = os.path.abspath(os.path.join(os.path.dirname(_file_),"..",".."))

INDEX_GROUPS = os.getenv("INDEX_GROUPS" ,"tweets")
ES_MAPPING = {
                "mappings": {
                    "properties": {
                        "TweetID": {"type": "Keyword"},
                        "CreateDate": {"type": "date", "ignore_malformed": True},
                        "Antisemitic": {"type": "boolean"},
                        "text": {"type": "text"}
                    }
                }
            }


