import os
import boto3
import time
from flask import Blueprint, request
from ..models import db
from ..models.users import User
from ..models.posts import Post

bp = Blueprint("aws", __name__, url_prefix="/api/aws")

UPLOAD_FOLDER = "uploads"
BUCKET = "elbows"

@bp.route("/<int:userId>", methods=["POST"])
def upload_post(userId):
    if request.method == "POST":
        print(request.files['file'])
        f = request.files['file']
        f.filename = change_name(f.filename)
        f.save(os.path.join(UPLOAD_FOLDER, f.filename))
        upload_file(f"uploads/{f.filename}", BUCKET)
        image_url = f"https://elbows.s3.us-east-2.amazonaws.com/uploads/{f.filename}"

        return {"post": "success"}


def upload_file(file_name, bucket):
    """
    Function to upload a file to an S3 bucket
    """
    object_name = file_name
    s3_client = boto3.client('s3')
    response = s3_client.upload_file(file_name, bucket, object_name)

    return response

def change_name(file_name):
    return f"{time.ctime().replace(' ', '').replace(':', '')}.png"



