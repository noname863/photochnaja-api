import os

SECRET_KEY = '\xb2d\xd3\xad\xbb\x84\r\xd5\xa8\xd7R\x0b\xbf\xb7\xb8\xf7\xd0SF\xabw\xfd\xa9!'

############
# DATABASE #
############

DATABASE_USER = os.getenv('DATABASE_USER')
if not DATABASE_USER:
    DATABASE_USER = 'sa'

DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
if not DATABASE_PASSWORD:
    DATABASE_PASSWORD = 'password1/'

DATABASE_HOST = os.getenv('DATABASE_HOST')
if not DATABASE_HOST:
    DATABASE_HOST = 'localhost'

DATABASE_PORT = os.getenv('DATABASE_PORT')
if not DATABASE_PORT:
    DATABASE_PORT = '1433'

DATABASE_NAME = os.getenv('DATABASE_NAME')
if not DATABASE_NAME:
    DATABASE_NAME = 'photochnaja_db'

DATABASE_DRIVER = os.getenv('DATABASE_DRIVER')
if not DATABASE_DRIVER:
    DATABASE_DRIVER = 'ODBC+Driver+17+for+SQL+Server'

SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://{}:{}@{}:{}/{}?driver={}'.format(
    DATABASE_USER, DATABASE_PASSWORD, DATABASE_HOST, DATABASE_PORT,
    DATABASE_NAME, DATABASE_DRIVER)

# Database variables for tests

TEST_DATABASE_NAME = os.getenv('TEST_DATABASE_NAME')
if not TEST_DATABASE_NAME:
    TEST_DATABASE_NAME = 'photochnaja_db_test'

TEST_DATABASE_URI = 'mssql+pyodbc://{}:{}@{}:{}/{}?driver={}'.format(
    DATABASE_USER, DATABASE_PASSWORD, DATABASE_HOST, DATABASE_PORT,
    TEST_DATABASE_NAME, DATABASE_DRIVER)

# Initial database variables
INITIAL_DATABASE_NAME = os.getenv('INITIAL_DB_NAME')
if not INITIAL_DATABASE_NAME:
    INITIAL_DATABASE_NAME = 'master'

INITIAL_DATABASE_URI = 'mssql+pyodbc://{}:{}@{}:{}/{}?driver={}'.format(
    DATABASE_USER, DATABASE_PASSWORD, DATABASE_HOST, DATABASE_PORT,
    INITIAL_DATABASE_NAME, DATABASE_DRIVER)

###########
# STORAGE #
###########

STORAGE_CONNECTION_STRING = os.getenv('STORAGE_CONNECTION_STRING')
if not STORAGE_CONNECTION_STRING:
    STORAGE_CONNECTION_STRING = 'DefaultEndpointsProtocol=http;AccountName=devstoreaccount1;AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;BlobEndpoint=http://127.0.0.1:10000/devstoreaccount1;QueueEndpoint=http://127.0.0.1:10001/devstoreaccount1;'
