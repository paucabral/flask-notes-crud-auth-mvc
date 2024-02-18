import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Load the configuration based on the environment
    if os.environ.get('FLASK_ENV') == 'production':
        SECRET_KEY = os.getenv("PROD_SECRET_KEY")
        SQLALCHEMY_DATABASE_URI = os.getenv("PROD_DB_URI")
    elif os.environ.get('FLASK_ENV') == 'staging':
        SECRET_KEY = os.getenv("STG_SECRET_KEY")
        SQLALCHEMY_DATABASE_URI = os.getenv("STG_DB_URI")
    elif os.environ.get('FLASK_ENV') == 'test':
        SECRET_KEY = os.getenv("TEST_SECRET_KEY")
        SQLALCHEMY_DATABASE_URI = os.getenv("TEST_DB_URI")
    else:
        SECRET_KEY = os.getenv("DEV_SECRET_KEY")
        SQLALCHEMY_DATABASE_URI = os.getenv("DEV_DB_URI")
    # Add other configurations as needed for production and testing

    @staticmethod
    def init_app(app):
        pass