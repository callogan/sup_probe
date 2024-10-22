import secrets
import string
from datetime import date, timedelta


class InvitationEntity:
    DAYS = 7

    def get_invitation_code(self):
        return self.generate_code()

    def generate_code(self, length=20):
        character_sheet = string.ascii_letters + string.digits
        rand_code = "".join(secrets.choice(character_sheet) for i in range(length))
        print(f"https://www.google.ru/registration/{rand_code}")
        return rand_code

    def generation_date(self):
        dates = date.today() + timedelta(days=self.DAYS)
        return dates
