import io
import json
import uuid
from typing import Optional

import boto3

from simpl_utils.clients.s3 import S3
from simpl_utils.config import aws_default_bucket
from app.utils.logger import logger
from app.utils.config import get_config

logger = logger()


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

    def upload_file_to_s3(self, file_path) -> Optional[str]:

        try:
            s3_object_key = self.unique_payload_filename

            s3_client = boto3.client(
                service_name='s3',
                region_name=get_config('AWS_DEFAULT_REGION'),
                aws_access_key_id=get_config('AWS_ACCESS_KEY_ID'),
                aws_secret_access_key=get_config('AWS_SECRET_ACCESS_KEY')
            )

            response = s3_client.upload_file(file_path, get_config('AWS_BUCKET'), s3_object_key)

            bucket_location = boto3.client('s3').get_bucket_location(Bucket=get_config('AWS_BUCKET'))
            object_url = "https://s3-{0}.amazonaws.com/{1}/{2}".format(
                bucket_location['LocationConstraint'],
                get_config('AWS_BUCKET'),
                s3_object_key)

            return object_url

        except Exception as e:  # noqa
            logger.error(f'Error while uploading file to s3 payload: {file_path}')
            return None
