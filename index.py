import json

def lambda_handler(event, context):
    # TODO implement
    return [
        {
            "streamId": 101,
            "genre": "Top 40",
            "bitrate": 128
        },
        {
            "streamId": 102,
            "genre": "Top 40",
            "bitrate": 192
        }
    ]