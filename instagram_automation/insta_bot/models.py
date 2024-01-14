from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class account_details(models.Model):
    username = models.CharField(max_length=400)
    password = models.CharField(max_length=400)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    follow_status=models.BooleanField(default=False)
    unfollow_status=models.BooleanField(default=False)
    post_status=models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.name
    





class follow_accounts(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    acc= models.ForeignKey(account_details, on_delete=models.CASCADE)
    username = models.CharField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Default ordering by creation timestamp, earliest first
        ordering = ['created_at']

    def __str__(self):
        return self.username
    
    def __str__(self):
        return self.username

class directory_links(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    acc= models.ForeignKey(account_details, on_delete=models.CASCADE)
    link = models.CharField(max_length=400)
    
    def __str__(self):
        return self.link
    
class monitor_follow(models.Model):

    acc= models.ForeignKey(account_details, on_delete=models.CASCADE)
    followcounter = models.IntegerField(default=0)
    # def __str__(self):
    #     return self.followcounter
    
class images(models.Model):
    acc=models.ForeignKey(account_details, on_delete=models.CASCADE)
    image=models.CharField(max_length=400)
    

