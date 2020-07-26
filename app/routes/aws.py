import os
import boto3
from random import randrange
from flask import Blueprint, request
from ..models import db
from ..models.users import User
from ..models.posts import Post
from botocore.exceptions import ClientError
import logging

bp = Blueprint("aws", __name__, url_prefix="/api/aws")

UPLOAD_FOLDER = "uploads"
BUCKET = "elbows"

@bp.route("/presign/<object_name>")
def create_presigned_post(object_name, bucket_name=BUCKET,
                          fields=None, conditions=None, expiration=3600):
    s3_client = boto3.client('s3')
    try:
        file_name, mime_type = object_name.split(".")
        object_name = f"uploads/{randrange(1000)}.{mime_type}"
        response = s3_client.generate_presigned_post(bucket_name,
                                                     object_name,
                                                     Fields=fields,
                                                     Conditions=conditions,
                                                     ExpiresIn=expiration)
        response["fileUrl"] = f"https://elbows.s3.us-east-2.amazonaws.com/{object_name}"
    except ClientError as e:
        logging.error(e)
        return None
    # print(response)
    return response


# @bp.route("/<int:userId>", methods=["POST"])
# def upload_post(userId):
#     if request.method == "POST":
#         print(request.files['file'])
#         f = request.files['file']
#         f.save(os.path.join(UPLOAD_FOLDER, f.filename))
#         upload_file(f"uploads/{f.filename}", BUCKET)
#         # image_url = f"https://elbows.s3.us-east-2.amazonaws.com/uploads/{f.filename}"

#         return {"post": "success"}



# def upload_file(file_name, bucket):
#     """
#     Function to upload a file to an S3 bucket
#     """
#     object_name = file_name
#     s3_client = boto3.client('s3')
#     response = s3_client.upload_file(file_name, bucket, object_name)

#     return response






