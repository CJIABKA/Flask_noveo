import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or b':\x9f\xa6\xc3:32\xf514\xfc\x9b\xbb\xd9\xf9o'
