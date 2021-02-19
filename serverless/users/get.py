import os
import json

from users import utils
dynamodb = utils.dynamodb()


def get(event, context):
    """
    Get a user

    Args:
        event ([type]): [description]

    Returns:
        Dict: The data response
    """

    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    # fetch todo from the database
    result = table.get_item(
        Key={
            'id': event['pathParameters']['id']
        }
    )

    # create a response
    response = {
        'statusCode': 200,
        'body': json.dumps(result['Item'], cls=utils.DecimalEncoder),
        'headers': {
            'Access-Control-Allow-Headers' : 'Content-Type,X-Amz-Date,      Authorization,X-Api-Key,X-Amz-Security-Token',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        }
    }

    return response