from typing import Any, Optional
from django.core.management.base import BaseCommand
from apps.blog.models import Blog,User


class Command(BaseCommand):
    help = "populate Blogs"

    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        
        try:
            user = User.objects.first()
            if user is None:
                raise Exception("Seed Users First")
            blogs = [ 
                Blog(title="Demo1", body="Demo2", author=user),
                Blog(title="Demo2", body="Demo22", author=user),
                Blog(title="Demo3", body="Demo23", author=user),
                Blog(title="Demo4", body="Demo24", author=user),
                Blog(title="Demo5", body="Demo25", author=user)
            ]
            for blog in blogs:
                blog.save()
            print("Blog Seeded Successfully!")
        except Exception as e:
            print(str(e))
        