import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb('vistorCounter')
def lambda_handler(event, context):

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            # "location": ip.text.replace("\n", "")
        }),
    }
