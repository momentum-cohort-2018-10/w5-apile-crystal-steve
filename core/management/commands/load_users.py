from django.core.management.base import BaseCommand
import random

class Command(BaseCommand):

    help = "Loads Users and Links clears existing data."

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        from django.contrib.auth.models import User
        from mimesis import Person

        print("deleting users")
        User.objects.filter(is_superuser=False).delete()

        users = []
        person = Person()
        for _ in range(10):
            user = User.objects.create_user(person.username(), person.email(), 
                                            'password')
            users.append(user)
    
        print("Users Created")

        from core.models import Post
        from mimesis import Generic

        print("Deleting posts ..")
        Post.objects.all().delete() # WHY 

        posts = []
        generic = Generic('en')

        for _ in range(20):
            user = users[0]
            # user = users[random.randint(1,10)]
            post = Post.objects.create(author=user, title='test title', description='test',url='www.google.com',slug=random.randint(1,1000) )
            # post = Post.objects.create(**post_data)
            posts.append(post)
        print("Post Loaded")
