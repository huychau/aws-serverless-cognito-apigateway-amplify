import json
import time
import uuid
import boto3


# This is a workaround for: http://bugs.python.org/issue16535
class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return int(obj)
        return super(DecimalEncoder, self).default(obj)


def dynamodb():
    return boto3.resource('dynamodb')


def get_current_time():
    return str(time.time())


def get_uuid():
    return str(uuid.uuid1())
