import cloudinary
from decouple import config


CLOUDINARY_CLUOD_NAME = config('CLOUDINARY_CLUOD_NAME')
CLOUDINARY_PUBLIC_KEY = config('CLOUDINARY_PUBLIC_KEY')
CLOUDINARY_SECRET_KEY = config('CLOUDINARY_SECRET_KEY')




def cloudinary_init():
    cloudinary.config( 
        cloud_name = CLOUDINARY_CLUOD_NAME,
        api_key = CLOUDINARY_PUBLIC_KEY,
        api_secret = CLOUDINARY_SECRET_KEY,
        secure=True
    )