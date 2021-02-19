import json
import logging
import os

from users import utils
dynamodb = utils.dynamodb()


def create(event, context):
    """
    Create a new user

    Args:
        event ([type]): [description]

    Returns:
        Dict: The data response
    """

    data = json.loads(event['body'])
    
    if 'name' not in data or 'email' not in data or 'gender' not in data:
        logging.error('Validation Failed')
        raise Exception('Couldn\'t create a user.')
    
    timestamp = utils.get_current_time()

    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    item = {
        'id': utils.get_uuid(),
        'name': data['name'],
        'email': data['email'],
        'gender': data['gender'],
        'createdAt': timestamp,
        'updatedAt': timestamp,
    }

    # Write the user to the database
    table.put_item(Item=item)

    # create a response
    response = {
        'statusCode': 201,
        'body': json.dumps(item),
        'headers': {
            'Access-Control-Allow-Headers' : 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        }
    }

    return response