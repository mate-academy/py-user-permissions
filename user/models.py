from django.contrib.auth.models import AbstractUser
from django.db.models import UniqueConstraint


class User(AbstractUser):
    class Meta:
        constraints = [
            UniqueConstraint(fields=["username", "email"],
                             name="unique_user")
        ]
