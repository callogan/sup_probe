import asyncio
import aiosmtplib
from src.config.email import settings
from email.message import EmailMessage


class EmailService:

    async def send_message(self, to_email, subject, ms):
        message = EmailMessage()
        message["From"] = settings.smtp_server
        message["To"] = to_email
        message["Subject"] = subject
        message.set_content(ms)
        await aiosmtplib.send(
            message,
            hostname=settings.smtp_server,
            port=settings.smtp_port,
            username=settings.smtp_user,
            password=settings.smtp_password
        )





