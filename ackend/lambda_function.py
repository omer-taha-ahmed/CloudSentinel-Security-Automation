import urllib.request
import boto3
import os

def lambda_handler(event, context):
    # Update these variables in your AWS Lambda Environment settings
    SITE_URL = os.environ.get('SITE_URL') 
    SNS_ARN = os.environ.get('SNS_TOPIC_ARN')
    
    try:
        response = urllib.request.urlopen(SITE_URL, timeout=10)
        if response.getcode() == 200:
            return "Health Check Passed"
    except Exception as e:
        sns = boto3.client('sns')
        sns.publish(
            TopicArn=SNS_ARN,
            Subject="CloudSentinel Alert: Site Failure",
            Message=f"Automated check failed for {SITE_URL}. Error: {str(e)}"
        )
        return "Alert Sent"
