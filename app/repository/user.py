from gunicorn.config import User

from app.exceptions.user_metadata_repository import FetchOneUserMetadataException
from app.utils.logger import logger
from app.utils.postgresdb import prod_others_db_writer
from app.utils.singleton import Singleton

_log = logger()
GET_USER_BY_USER_ID = """SELECT * FROM Users WHERE id = %(user_id)s"""

class UserRepository(metaclass=Singleton):
    def __init__(self):
        self.db = prod_others_db_writer

    def get_user_by_user_id(self, user_id):
        try:
            record = self.db.fetch_one(
                GET_USER_BY_USER_ID, {"user_id": user_id}
            )
            if record is not None:
                user = User(**record)# change this as below
                # user = UserMetadata(
                #     phone_number=phone_number,
                #     has_transacted=record[1],
                #     onboarding_source=record[2]
                #     if record[2] is None
                #     else OnboardingSource(record[2]),
                #     has_completed_onboarding=record[3],
                #     has_waitlisted_onboarding=record[4],
                #     global_credit_lines=record[5],
                #     merchant_credit_lines=record[6],
                # )
                # change this with user model
                return user
            _log.info("No record found for user with id {}".format(user_id))
            return None
        except Exception as ex:
            raise FetchOneUserMetadataException(ex, user_id)

