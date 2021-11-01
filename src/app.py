import json
from create_user_address import create_user_address
from get_address_details import get_address_details
from get_user_addresses import get_user_addresses
from get_user_details import get_user_details
from sync_addresses import sync_addresses

def default():
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Invalid Path",
            # "location": ip.text.replace("\n", "")
        }),
    }

def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """
    handler_map = {
        "/create_user_address":  create_user_address,
        "/get_address_details": get_address_details,
        "/get_user_addresses": get_user_addresses,
        "/get_user_details": get_user_details,
        "/sync_addresses": sync_addresses
    }
    response = handler_map.get(event['resource'], default)
    return response(event)