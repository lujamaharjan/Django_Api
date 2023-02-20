
from typing import Any, Optional
from django.core.management.base import BaseCommand
from apps.blog.models import User


class Command(BaseCommand):
    help = "populate User"

    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        
        try:
            username = input("Enter Username: ")
            email = input("Enter Email: ")
            password = input("Enter Password: ")
            user = User.objects.create_user(username=username,
                                 email=email,
                                 password=password)
            user.save();
            print("User Seeded Successfully!")
        except Exception as e:
            print(str(e))
        