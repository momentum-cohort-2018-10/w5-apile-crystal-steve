from django.core.management.base import BaseCommand

# initial_posts = {
#     {
#         "title":
#         "My Boy Blue",
#         "author":
#         "Will Ferril",
#         "description":
#         "A homeless man is adopted by a band of fratboy misfits and becomes a pop cultre legend!",
#         "url":
#         "https://www.oldschoool.io/",
#     }
# }


class Command(BaseCommand):
    help = "Loads Users and Links clears existing data."

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        # from core.models import Post
        # print("Deleting posts ..")
        # Post.objects.all().delete()

        # posts = []
        # for post_data in initial_posts:
        #     post = Post.objects.create(**post_data)
        #     posts.append(post)
        # print("Post Loaded")


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
