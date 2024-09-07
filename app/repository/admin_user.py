from app.exceptions.repository_exceptions import FetchOneUserMetadataException
from app.models.admin_type import AdminType
from app.models.admin_user import AdminUser
from app.utils.logger import logger
from app.utils.postgresdb import prod_others_db_writer
from app.utils.singleton import Singleton

_log = logger()
GET_USER_BY_USER_ID = """SELECT * FROM admin WHERE user_id = %(user_id) order by created_at desc"""
SAVE_USER = """INSERT INTO admin (type, user_id, password) values (%(type), %(user_id), %(password))"""
DELETE_USER = """DELETE * FROM admin WHERE user_id = %(user_id)"""


class AdminUserRepository(metaclass=Singleton):
    def __init__(self):
        self.db = prod_others_db_writer

    def get_user_by_user_id(self, user_id: str):
        try:
            record = self.db.fetch_one(
                GET_USER_BY_USER_ID, {"user_id": user_id}
            )
            if record is not None:
                user = AdminUser(
                    admin_type=record[2],
                    user_id=record[3],
                    password=record[4],
                    created_at=record[5]
                )
                return user
            _log.info("No record found for admin with with user_id {}".format(user_id))
            return None
        except Exception as ex:
            raise FetchOneUserMetadataException(ex, user_id)

    def save_user(self, admin_type: AdminType, user_id: str, password: str) -> bool:
        try:
            record = self.db.execute(
                SAVE_USER, {"type": admin_type.value, "user_id": user_id, "password": password}
            )
            if record is not None:
                return True
            else:
                _log.info("Unable to save record for admin with user_id {}".format(user_id))
                return False

        except Exception as ex:
            raise FetchOneUserMetadataException(ex, user_id)

    def delete_user(self, user_id: str) -> bool:
        try:
            record = self.db.execute(
                DELETE_USER, {"user_id": user_id}
            )
            if record is not None:
                return True
            else:
                _log.info("Unable to delete record for admin with user_id {}".format(user_id))
                return False

        except Exception as ex:
            raise FetchOneUserMetadataException(ex, user_id)
