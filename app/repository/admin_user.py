from app.exceptions.repository_exceptions import FetchOneUserMetadataException
from app.models.admin_user import AdminUser
from app.utils.logger import logger
from app.utils.postgresdb import prod_others_db_writer
from app.utils.singleton import Singleton

_log = logger()
GET_USER_BY_USER_ID = """SELECT * FROM admin WHERE user_id = %(user_id) order by created_at desc"""


class AdminUserRepository(metaclass=Singleton):
    def __init__(self):
        self.db = prod_others_db_writer

    def get_user_by_user_id(self, user_id):
        try:
            record = self.db.fetch_one(
                GET_USER_BY_USER_ID, {"user_id": user_id}
            )
            if record is not None:
                user = AdminUser(
                    admin_type=record[1],
                    user_id=record[2],
                    password=record[3],
                    phone_number=record[4],
                    email=record[5],
                    created_at=record[6]
                )
                return user
            _log.info("No record found for user with id {}".format(user_id))
            return None
        except Exception as ex:
            raise FetchOneUserMetadataException(ex, user_id)
