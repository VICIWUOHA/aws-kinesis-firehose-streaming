## AWS Kinesis Firehose Data Streaming

**Author: *Victor Iwuoha***



### Overview
This script streams simulated order data to an AWS Kinesis Firehose delivery stream. Generation  of random order dictionaries is done using a 
`generate_order()` function powered by Faker library. It adds a timestamp and prints each order before sending it to the Firehose stream using the AWS SDK boto3 client. Exceptions are caught and printed for debugging.

**Requirements**
Python 3
Boto3
AWS credentials configured with IAM permissions for Kinesis Firehose

### Usage

- Configure AWS credentials and region in a .env file
- Run `python3 -m pip install -r requirements.txt`
- Run `python3 stream.py`


#### Configuration
The AWS credentials, region, and Firehose delivery stream name are read from environment variables defined in a `.env` file.