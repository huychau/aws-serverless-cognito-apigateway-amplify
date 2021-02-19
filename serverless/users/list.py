import json
import os

from users import utils
dynamodb = utils.dynamodb()


def list(event, context):
    """
    List all users

    Args:
        event ([type]): [description]

    Returns:
        Dict: The data response
    """

    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    # Fetch all users from the database
    result = table.scan()

    # Create a response
    response = {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers' : 'Content-Type,X-Amz-Date,      Authorization,X-Api-Key,X-Amz-Security-Token',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        'body': json.dumps(result['Items'], cls=utils.DecimalEncoder),

    }

    return response