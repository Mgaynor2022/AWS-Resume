import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb('vistorCounter')

def lambda_handler(event, context):
    
    response = table.get_item( key= {
        'id':'1'
    })
    visitor = response['item']['visitor']
    visitor = visitor + 1
    print(visitor)

    response = table.put_item(item = {
        'id':'2',
        'visitor': visitor
    })
    return visitor

    # return {
    #     "statusCode": 200,
    #     "body": json.dumps({
    #         "message": "hello world",
    #         # "location": ip.text.replace("\n", "")
    #     }),
    # }
