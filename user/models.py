from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    @staticmethod
    def validate_password(password: str):
        if len(password) < 5:
            raise ValueError(
                "Password must be more than or equal to 5 symbols."
            )
