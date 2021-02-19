import os

from users import utils
dynamodb = utils.dynamodb()


def delete(event, context):
    """
    Delete a user

    Args:
        event ([type]): [description]

    Returns:
        Dict: The data response
    """

    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    # delete the todo from the database
    table.delete_item(
        Key={
            'id': event['pathParameters']['id']
        }
    )

    # create a response
    response = {
        'statusCode': 204,
        'headers': {
            'Access-Control-Allow-Headers' : 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,PUT,DELETE,GET'
        }
    }

    return response