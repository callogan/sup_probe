from src.apps.email.service import EmailService
from typing import Annotated
from fastapi import Depends


IEmailService = Annotated[EmailService, Depends()]
