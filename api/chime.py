import boto3
import sys

sys.path.append('../')
import cosmos

REGION = "ap-northeast-1"

client = client = boto3.client('chime')

# データベースからmeeting情報が存在するドキュメントを取り出す。
def getMeeting(meetingTitle: str):
    return dict