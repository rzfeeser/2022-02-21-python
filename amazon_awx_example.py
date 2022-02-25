#!/usr/bin/python3
"""Alta3 Research | RZFeeser@alta3.com
   Using boto3 to connect to aws"""

import boto3


# Let's use Amazon S3
s3 = boto3.resource('s3')

# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)
