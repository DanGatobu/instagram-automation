from django.test import TestCase

# test_celery_tasks.py
from .tasks import  instabot

# Call the clogin task for a specific account ID


# Call the follow_post_unfollow task for a specific account ID
instabot.delay()


# Create your tests here.
