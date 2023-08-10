from pydantic import BaseSettings

class Settings(BaseSettings):
# """
# Define settings for the mail, server, redis connections
# """

    sqlalchemy_database_url: str = "postgresql+psycopg2://postgres:567234@localhost:5432/rest_app"
    secret_key: str = "key"
    algorithm: str = "alg"
    mail_username: str = "user"
    mail_password: str = "pass"
    mail_from: str = "mail@mail.com"
    mail_port: int = 465
    mail_server: str = "smt.mail.com"
    redis_host: str = 'localhost'
    redis_port: int = 6379
    cloudinary_name: str = "name"
    cloudinary_api_key: str = "key"
    cloudinary_api_secret: str = "secret"
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()