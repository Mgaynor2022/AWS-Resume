import json
import boto3

# import requests

# dynamodb = boto3.resource('dynamodb')
# table = dynamodb.Table('VisitorCount')

# def lambda_handler(event, context):
#     response = table.get_item(Key = {
#         'id': '0'
#     })
#     visitor = response['item']['visitor']
#     visitor = visitor + 1
#     print(visitor)

#     response = table.put_item(Item = {
#         'id':'0',
#         'visitor':'visitor'
#     })
#     return visitor
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('VisitorCount')

def lambda_handler(event, context):
    # Retrieve data
    response = table.get_item(Key={
        'id': 'count'
    })
    response = response['Item'],['visitor']

    # Increment visitor count
    visitor_count = response.get('Item', {}).get('visitor', 0) + 1
    print(visitor_count)

    # Update data
    response = table.update_item(Item={
        'id': '0',
        'visitor': visitor_count
    })

    return {
        'statusCode': 200,
        'body': str(visitor_count)
    }



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

    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e

    # return {
    #     "statusCode": 200,
    #     "body": json.dumps({
    #         "message": "hello world",
    #         # "location": ip.text.replace("\n", "")
    #     }),
    # }
