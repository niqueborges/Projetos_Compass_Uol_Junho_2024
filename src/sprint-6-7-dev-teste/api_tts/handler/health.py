import json


def health(event, context):
    body ={
        "message": "Go Serverless v4.0! Your function executed successfully!",
        "input": event,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response
