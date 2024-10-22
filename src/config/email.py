from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # credentials
    smtp_user: str = Field(..., alias="SMTP_USER")
    smtp_password: str = Field(..., alias="SMTP_PASSWORD")
    smtp_port: int = Field(587, alias="SMTP_PORT")
    smtp_server: str = Field("smtp.gmail.com", alias="SMTP_HOST")


settings = Settings()
