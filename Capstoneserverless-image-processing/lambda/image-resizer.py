import boto3
from PIL import Image
import os
import json

s3 = boto3.client("s3")


RESIZED_BUCKET = "capstone-resized-images-ruchit"

def lambda_handler(event, context):
    try:
        bucket = event["bucket"]
        key = event["key"]

        download_path = f"/tmp/{os.path.basename(key)}"
        resized_path = f"/tmp/resized-{os.path.basename(key)}"

        s3.download_file(bucket, key, download_path)

        with Image.open(download_path) as img:
            img.thumbnail((128, 128))
            img.save(resized_path)

        s3.upload_file(resized_path, RESIZED_BUCKET, key)

        return {
            "success": True,
            "message": "Image resized successfully",
            "outputBucket": RESIZED_BUCKET,
            "file": key
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }