# Capstoneproject-Imageresizer
Serverless Image Pipeline 
## Overview

This project implements a serverless image processing pipeline on AWS using:
- Amazon S3
- AWS Lambda Python + Pillow
- AWS Step Functions
- Amazon API Gateway
- Amazon CloudWatch

When a user uploads an image to the original S3 bucket and calls the API endpoint,
the system resizes the image to a thumbnail and stores it in the resized S3 bucket.

## Architecture

1. Original image uploaded to S3.
2. API Gateway endpoint '/process' receives 'bucket' and 'key'.
3. API Gateway calls Step Functions 'StartExecution'.
4. Step Functions calls a Lambda function 'CapstoneImageResizer'.
5. Lambda downloads the original image from S3, resizes it using Pillow, and uploads it to the resized bucket.
6. Step Functions returns success or failure.

## Buckets

- Original images bucket: 'capstone-original-images-ruchit'
- Resized images bucket: 'capstone-resized-images-ruchit'

## Lambda

- Name: 'CapstoneImageResizer'
- Runtime: Python 3.12
- Uses Pillow library via a Lambda Layer.
- Input JSON format:
{
  "bucket": "capstone-original-images-yourname",
  "key": "image-file-name.jpg/png"
}
