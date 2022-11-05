import logging

import azure.functions as func
import boto3

REGION = "ap-northeast-1"

def main(req: func.HttpRequest) -> func.HttpResponse:
    client = boto3.client('chime')

    # TODO
    meetingId: str = req.params.get('meeting')
    attendeesId: str = req.params.get('attendeesId')

    meetingInfo: dict
    try:
        meetingInfo = client.get_meeting(meetingId)
    except client.exceptions.NotFoundException:
        print(meetingId + ' is not found. so create it')
        meetingInfo = client.create_meeting(
            ClientRequestToken=meetingId,
            MediaRegion=REGION,
            ExternalRequestId=meetingId,
        )
    except:
        raise

    try:
    except:

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
