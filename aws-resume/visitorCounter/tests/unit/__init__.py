import json

def eventTest (event, context):
    first_name = event['first_name']
    last_name = event['last_name']
    action = event['action']

    return {
        'statusCode': 200,
        'body': json.dumps({
            'action': f"{first_name} {last_name} {action}"
        })
    }
