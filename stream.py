# Script for Ingestinting into kinesis firehose stream
import os
import boto3
from time import sleep
from datetime import datetime
from dotenv import load_dotenv
from assets.DataGenerator import generate_order


load_dotenv(override=True)

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_DEFAULT_REGION = os.getenv("AWS_DEFAULT_REGION")
AWS_FIREHOSE_STREAM_NAME = os.getenv("AWS_FIREHOSE_STREAM_NAME")


client = boto3.client(
    "firehose",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_DEFAULT_REGION,
)


# simulate order generation with an infinte while loop.
stream_count = 0

while True:
    try:
        order = generate_order()
        order["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(order)
        response = client.put_record(
            DeliveryStreamName=AWS_FIREHOSE_STREAM_NAME,
            Record={"Data": bytes(str(order), "utf-8")},
        )
        print(response["ResponseMetadata"]["HTTPStatusCode"])
        # sleep for some seconds to avoid hitting the rate limit
        sleep(5)
        # break out of the loop after 10 orders
        if stream_count == 10:
            break
        stream_count += 1
        print(f"==>>>>>`{stream_count}` record(s) streamed so far....")
    except Exception as e:
        print(e)
        raise e
