import json
import logging
import os

from users import utils
dynamodb = utils.dynamodb()


def update(event, context):
    """
    Update user

    Args:
        event ([type]): [description]

    Returns:
        Dict: The data response
    """

    data = json.loads(event['body'])

    # Make sure all attributes are not empty
    if 'name' not in data or 'email' not in data or 'gender' not in data:
        logging.error('Validation Failed')
        raise Exception('Couldn\'t update the user.')
        return

    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    # update the user in the database
    result = table.update_item(
        Key={
            'id': event['pathParameters']['id']
        },
        ExpressionAttributeValues={
            ':name': data['name'],
            ':email': data['email'],
            ':gender': data['gender'],
            ':updatedAt': utils.get_current_time(),
        },
        UpdateExpression='SET name = :name, '
                        'email = :email, '
                        'gender = :gender, '
                        'updatedAt = :updatedAt',
        ReturnValues='ALL_NEW',
    )

    # create a response
    response = {
        'statusCode': 200,
        'body': json.dumps(result['Attributes'], 
                            cls=utils.DecimalEncoder),
        'headers': {
            'Access-Control-Allow-Headers' : 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,PUT,DELETE,GET'
        }
    }

    return response