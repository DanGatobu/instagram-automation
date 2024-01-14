from instagram_automation.celery import Celery
import time as tt
import random
from django.shortcuts import get_object_or_404
from selenium import webdriver
import logging

from .functions import follow,login,unfollow,postpicture
from .models import account_details,follow_accounts,monitor_follow,images,directory_links
import os 
app = Celery('instagram_automation')

app = Celery('tasks', broker='pyamqp://guest@localhost//')

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def cfollow(driver,idd):
    account=account_details.objects.get(id=idd)
    acc=follow_accounts.objects.filter(acc=account)
    follow_count,k=monitor_follow.objects.get_or_create(acc=account)
    if follow_count.followcounter>len(acc)-1:
        follow_count.followcounter=0
        follow_count.save()
    profile=acc[follow_count.followcounter]
    follow_count.followcounter=follow_count.followcounter+1
    follow_count.save()
    login(driver,account.username,account.password)
    tt.sleep(5)
    follow(driver,profile.username)
    

def follow_post_unfollow(driver,idd):
    account=account_details.objects.get(id=idd)
    accountobj=get_object_or_404(account_details, pk=idd)
    acc=follow_accounts.objects.filter(acc=account)
    dp=directory_links.objects.get(acc=account)
    
    follow_count,k=monitor_follow.objects.get_or_create(acc=account)
    if follow_count.followcounter>len(acc)-1:
        follow_count.followcounter=0
        follow_count.save()
    profile=acc[follow_count.followcounter]
    follow_count.followcounter=follow_count.followcounter+1
    follow_count.save()
    login(driver,account.username,account.password)
    tt.sleep(5)
    functions_to_execute = [follow, postpicture, unfollow]
    file_list = os.listdir(dp.link)
    random.shuffle(functions_to_execute)
    tt.sleep(5)
    for func in functions_to_execute:
        if func == follow:
            func(driver,profile.username)
            tt.sleep(3)
        elif func == postpicture:
            for file in file_list:
                if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff')):
                    if not images.objects.filter(acc=account, image=file.lower()).exists():
                        link=os.path.join(dp.link, file)
                        link = r'{}'.format(link)
                        func(driver,link)
                        images.objects.create(acc=accountobj,image=file.lower())
                        break
                        
                        
                    
            
            tt.sleep(4)
        elif func == unfollow:
            func(driver,20,account.username)

def post_unfollow(driver,idd):
    account=account_details.objects.get(id=idd)
    accountobj=get_object_or_404(account_details, pk=idd)
    acc=follow_accounts.objects.filter(acc=account)
    dp=directory_links.objects.get(acc=account)
    
    follow_count,k=monitor_follow.objects.get_or_create(account)
    if follow_count.followcounter>len(acc)-1:
        follow_count.followcounter=0
        follow_count.save()
    profile=acc[follow_count.followcounter]
    follow_count.followcounter=follow_count.followcounter+1
    follow_count.save()
    login(driver,account.username,account.password)
    tt.sleep(5)
    functions_to_execute = [postpicture, unfollow]
    file_list = os.listdir(dp.link)
    random.shuffle(functions_to_execute)
    tt.sleep(5)
    for func in functions_to_execute:
        
        if func == postpicture:
            for file in file_list:
                if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff')):
                    if not images.objects.filter(acc=account, image=file.lower()).exists():
                        link=os.path.join(dp.link, file)
                        link = r'{}'.format(link)
                        func(driver,link)
                        images.objects.create(acc=accountobj,image=file.lower())
                        break
                        
            tt.sleep(4)
        elif func == unfollow:
            func(driver,20,account.username)
        
                      
def follow_unfollow(driver,idd):  
    account=account_details.objects.get(id=idd)
    accountobj=get_object_or_404(account_details, pk=idd)
    acc=follow_accounts.objects.filter(acc=account)
    follow_count,k=monitor_follow.objects.get_or_create(acc=account)
    if follow_count.followcounter>len(acc)-1:
        follow_count.followcounter=0
        follow_count.save()
    profile=acc[follow_count.followcounter]
    follow_count.followcounter=follow_count.followcounter+1
    follow_count.save()
    login(driver,account.username,account.password)
    tt.sleep(5)
    functions_to_execute = [follow, unfollow]
    random.shuffle(functions_to_execute)
    tt.sleep(5)
    for func in functions_to_execute:
        if func == follow:
            func(driver,profile.username)
            tt.sleep(3)
                    
            tt.sleep(4)
        elif func == unfollow:
            func(driver,20,account.username)
    

def follow_post(driver,idd):  
    account=account_details.objects.get(id=idd)
    accountobj=get_object_or_404(account_details, pk=idd)
    acc=follow_accounts.objects.filter(acc=account)
    dp=directory_links.objects.get(acc=account)
    follow_count,k=monitor_follow.objects.get_or_create(acc=account)
    
    if follow_count.followcounter>len(acc)-1:
        follow_count.followcounter=0
        follow_count.save()
    profile=acc[follow_count.followcounter]
    follow_count.followcounter=follow_count.followcounter+1
    follow_count.save()
    login(driver,account.username,account.password)
    tt.sleep(5)
    functions_to_execute = [follow, postpicture]
    file_list = os.listdir(dp.link)

    random.shuffle(functions_to_execute)


    tt.sleep(5)
    for func in functions_to_execute:
        if func == follow:
            func(driver,profile.username)
            tt.sleep(3)
        elif func == postpicture:
            for file in file_list:
                if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff')):
                    if not images.objects.filter(acc=account, image=file.lower()).exists():
                        link=os.path.join(dp.link, file)
                        link = r'{}'.format(link)
                        func(driver,link)
                        images.objects.create(acc=accountobj,image=file.lower())
                        break
                        
                        
                    
            
            tt.sleep(4)
        
    

def cunfollow(driver,idd):
    
    account=account_details.objects.get(id=idd)
    accountobj=get_object_or_404(account_details, pk=idd)
    dp=directory_links.objects.get(acc=account)
    
    login(driver,account.username,account.password)
    
    account=account_details.objects.get(id=idd)
    unfollow(driver,20,account.username)

  
def cpostpicture(driver,idd):
    account=account_details.objects.get(id=idd)
    accountobj=get_object_or_404(account_details, pk=idd)
    dp=directory_links.objects.get(acc=account)
    
    login(driver,account.username,account.password)
    tt.sleep(5)
    logger.info(f"Link: {dp.link}")

    file_list = os.listdir(dp.link)



    for file in file_list:
        if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff')):
            if not images.objects.filter(acc=account, image=file.lower()).exists():
                link=os.path.join(dp.link, file)
                link = r'{}'.format(link)
                postpicture(driver,link)
                images.objects.create(acc=accountobj,image=file.lower())
                break
                                     
@app.task
def instabot():
    logger.info("Starting instabot function")
    driver = webdriver.Chrome()
    accounts=account_details.objects.all()
    num_accounts = len(accounts)

    logger.info(f"Number of accounts: {num_accounts}")

    for account in accounts:
        
        if  account.post_status and not account.follow_status and not account.unfollow_status:
            idd=account.id
            cpostpicture(driver,idd)
            
        elif not account.post_status and not account.follow_status and account.unfollow_status:
            idd=account.id
            cunfollow(driver,idd)
        elif account.post_status and account.follow_status and not account.unfollow_status:
            idd=account.id
            follow_post(driver,idd)
        elif not account.post_status and  account.follow_status and account.unfollow_status:
            idd=account.id
            follow_unfollow(driver,idd)
        elif account.post_status and not account.follow_status and account.unfollow_status:
            idd=account.id
            post_unfollow(driver,idd)
        elif account.post_status and account.follow_status and account.unfollow_status:
            idd=account.id
            follow_post_unfollow(driver,idd)
        elif not account.post_status and account.follow_status and not account.unfollow_status:
            idd=account.id
            cfollow(driver,idd)
        
            
            
            