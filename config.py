import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "change-this-secret")

    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True

    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    RECEIVER_EMAIL = os.environ.get("RECEIVER_EMAIL")
