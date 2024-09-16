from app.exceptions.repository_exceptions import FetchOneUserMetadataException
from app.models.all_info import AllInfo
from app.utils.logger import logger
from app.utils.postgresdb import prod_others_db_writer
from app.utils.singleton import Singleton
import json

_log = logger()
GET_METADATA = """SELECT * FROM meta_data created_at desc"""
SAVE_METADATA = """INSERT INTO meta_data (data) values (%(data))"""


class MetaDataRepository(metaclass=Singleton):
    def __init__(self):
        self.db = prod_others_db_writer

    def get_latest_meta_data(self):
        try:
            record = self.db.fetch_one(
                GET_METADATA, {}
            )
            if record is not None:
                meta_data = json.loads(record[2], object_hook=AllInfo)
                return meta_data
            _log.info("No metadata found")
            return None
        except Exception as ex:
            raise FetchOneUserMetadataException(ex, None)

    def save_meta_data(self, json_output):
        try:

            record = self.db.execute(
                SAVE_METADATA, {"data": json.dumps(json_output)}
            )
            if record is not None:
                return True
            else:
                _log.info("Unable to save metadata")
                return False
        except Exception as ex:
            raise FetchOneUserMetadataException(ex, None)
