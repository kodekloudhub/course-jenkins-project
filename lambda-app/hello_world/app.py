import json

# import requests


def lambda_handler(event, context):


    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world v7",
            # "location": ip.text.replace("\n", "")
        }),
    }
