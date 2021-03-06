import os
dirname = os.path.dirname(__file__)

DEBUG = False
COMPRESS_RESPONSE = True
PORT = int(os.environ.get("PORT", 5000))
STATIC_PATH = os.path.join(dirname, '../assets')
TEMPLATE_PATH = os.path.join(dirname, '../templates')