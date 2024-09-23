import cloudinary
from django.conf import settings


CLOUDINARY_CLUOD_NAME = settings.CLOUDINARY_CLUOD_NAME
CLOUDINARY_PUBLIC_KEY = settings.CLOUDINARY_PUBLIC_KEY
CLOUDINARY_SECRET_KEY = settings.CLOUDINARY_SECRET_KEY


def cloudinary_init():
    cloudinary.config( 
        cloud_name = CLOUDINARY_CLUOD_NAME,
        api_key = CLOUDINARY_PUBLIC_KEY,
        api_secret = CLOUDINARY_SECRET_KEY,
        secure=True
    )