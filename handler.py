import json

def hello(event, context):
    body = {
        "message": "Your function executed successfully",
        "input": event,
    }

    return {"statusCode": 200, "body": json.dumps(body)}