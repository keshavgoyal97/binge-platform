import io
import json
import uuid

from simpl_utils.clients.s3 import S3
from simpl_utils.config import aws_default_bucket
from simpl_utils.logger import Logger

logger = Logger()


class S3Manager:

    def __init__(self):
        self.s3 = S3()

    @property
    def unique_payload_filename(self):
        """Return a unique filename for the payload"""
        random_string = uuid.uuid4().hex
        webhooks_folder = ''
        return f'{webhooks_folder}{random_string}.json'

    def publish_to_s3(self, payload):
        """Handle the webhook from clevertap and schedule the event

        Parse the payload from clevertap and create events for each user,
        and schedule a job to publish the event.
        """

        # Upload the file to s3
        s3_object_key = self.unique_payload_filename

        uploaded, err = self.s3.put_object(
            key=s3_object_key,
            bucket=aws_default_bucket,
            file_obj=io.BytesIO(json.dumps(payload).encode('utf-8')),
        )

        if err is not None:
            logger.error("Error while uploading payload {}".format(err))
            raise Exception("Error while uploading payload {}".format(err))
        return s3_object_key

    def get_object_from_s3(self, s3_object_key):

        try:
            response = self.s3.get_object(bucket=aws_default_bucket, key=s3_object_key)
            if not response:
                logger.error('Error while fetching payload')
                return None

            payload = json.loads(response['Body'].read().decode('utf-8'))
            return payload
        except json.JSONDecodeError:
            logger.error('Error while decoding payload')
            return None
        except Exception as e:  # noqa
            logger.error('Error while read payload: {}'.format(str(e)))
            return None
