from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError


class User(AbstractUser):
    @staticmethod
    def validate_password(password: str, error_to_show):
        if len(password) < 5:
            raise error_to_show({
                "password": "Password must be more than or equal to 5 symbols."
            })

    def clean(self):
        User.validate_password(
            self.password, ValidationError
        )
