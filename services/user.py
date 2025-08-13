from django.contrib.auth import get_user_model
from django.db.models import QuerySet

from db.models import User


def create_user(
    username: str,
    password: str,
    email: str = None,
    last_name: str = None,
    first_name: str = None,
) -> User:
    # User = get_user_model()

    extra_fields = {}
    if email:
        extra_fields["email"] = email
    if first_name:
        extra_fields["first_name"] = first_name
    if last_name:
        extra_fields["last_name"] = last_name

    user = User.objects.create_user(
        username=username,
        password=password,
        **extra_fields
    )
    return user


def get_user(user_id: int) -> User:
    return User.objects.get(id=user_id)
