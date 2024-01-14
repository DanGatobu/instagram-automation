from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages ,auth
from django.contrib.auth import authenticate ,login,logout
from django.contrib.auth.decorators import login_required
from .models import follow_accounts,account_details,directory_links
from .tasks import  instabot
from django.http import HttpResponse

from django.shortcuts import get_object_or_404
import random
import schedule

# Create your views here.


def testf(request):
    instabot.delay()
    return HttpResponse("Task started in the background.")

def index(request):
    
    
    return render(request, 'index.html',)

def redirect_to_home(request):
    return redirect('home')



def register(request):
    
    if request.method == "POST":
        email=request.POST.get('email')
        fname=request.POST.get('fname')
        sname=request.POST.get('sname')
        uname=request.POST.get('uname')   
        password=request.POST.get('pass')            #reemeber to add fuctionality since we using the user class
        password2=request.POST.get('repeatpass')
        if password==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'email already exists')
                return redirect('register')
            elif User.objects.filter(username=uname).exists():
                messages.info(request,'user already exists')
                return redirect('register')
        
            else:
                User.objects.create_user(first_name=fname,last_name=sname,username=uname,email=email,password=password)
                user = authenticate(request, username=uname, password=password)
                auth.login(request, user)
                
                request.session['firstname'] = fname
                request.session['username'] = uname
                return redirect('home')
                
        else:
            messages.info(request,'passwords do not match')
            return redirect('register')
    
    return render(request, 'register.html',)

def login(request):
        
    if request.method == "POST":
        uname=request.POST.get('uname')
        password=request.POST.get('pass')
        user=auth.authenticate(username=uname,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect ('login')
    else:
        return render(request,'login.html')
    
        print(email)
        
@login_required(login_url='login')
       
def logout(request):
    auth.logout()
    return render('login')

@login_required(login_url='login')
def accounts(request):
    
    acc=account_details.objects.filter(user=request.user)
    
    return render(request, 'accounts.html',{'acc':acc})
@login_required(login_url='login')
def control(request):
    uid=request.user.id
    acc=account_details.objects.filter(user=uid)
    return render(request, 'control.html',{'acc':acc})

@login_required(login_url='login')
def addaccount(request):
    if request.method == "POST":
        
        username=request.POST.get('username')
        # email=request.POST.get('email')
        password=request.POST.get('pass')
        password2=request.POST.get('repeatpass')
        if password==password2:
            if account_details.objects.filter(username=username).exists():
                messages.info(request,'user already exists')
                return redirect('addaccount')
            else:
                fc=account_details.objects.create(username=username,password=password,user=request.user)
                
                return redirect('accountsetup',fc.id)
        
        return redirect('accountsetup')
@login_required(login_url='login')
def delete_followaccount(request,account_id):
    da=follow_accounts.objects.get(id=account_id)
    da.delete()
    return redirect('accountsetup',int(request.session['accountid']))
 
#  def change_link(request,idd):
#      lin=get_object_or_404(directory_links,pk=idd)
#      lin.
     
 
        
@login_required(login_url='login')
def accountsetup(request,account_id):
    user_id = request.user.id
    f_accounts=follow_accounts.objects.filter(owner_id=user_id,acc=account_id)
    request.session['accountid'] = account_id
    link=directory_links.objects.filter(owner_id=user_id,acc=account_id)
    vals={'accounts':f_accounts,'link':link}
    
    return render(request,'accountsetup.html',vals)

@login_required(login_url='login')
def addfollowaccount(request):
    if request.method == "POST":
        
        username=request.POST.get('username')
        acou=get_object_or_404( account_details,pk=int(request.session['accountid']))
        follow_accounts.objects.create(owner_id=request.user.id,acc=acou,username=username)
        
        return redirect('accountsetup',int(request.session['accountid']))
    

@login_required(login_url='login')
def add_directorylink(request):
    if request.method == "POST":
        user_id = request.user.id
        
        link=request.POST.get('link')
        acou=get_object_or_404( account_details,pk=int(request.session['accountid']))
        directory_links.objects.create(owner_id=user_id,acc=acou,link=link)
        return redirect('accountsetup',int(request.session['accountid']))
    


@login_required(login_url='login')
def change_link(request):
    
    
    return render(request,'changelink.html')

@login_required(login_url='login')
def activate_follow(request,account_id):
    
    id=account_id
    account=get_object_or_404(account_details, pk=id)
    account.follow_status=True
    account.save()
    return redirect('control')
 
@login_required(login_url='login')   
def activate_unfollow(request,account_id):
    user_id = request.user.id
    id=account_id
    account=get_object_or_404(account_details, pk=id)
    account.unfollow_status=True
    account.save()
    return redirect('control')
    
@login_required(login_url='login')
def activate_post(request,account_id):
    user_id = request.user.id
    id=account_id
    account=get_object_or_404(account_details, pk=id)
    account.post_status=True
    account.save()
    return redirect('control')
 
@login_required(login_url='login')   
def deactivate_follow(request,account_id):
    user_id = request.user.id
    id=account_id
    account=get_object_or_404(account_details, pk=id)
    account.follow_status=False
    account.save()
    return redirect('control')

@login_required(login_url='login')
def deactivate_unfollow(request,account_id):
    user_id = request.user.id
    id=account_id
    account=get_object_or_404(account_details, pk=id)
    account.unfollow_status=False
    account.save()
    
    return redirect('control')

@login_required(login_url='login')
def deactivate_post(request,account_id):
    user_id = request.user.id
    id=account_id
    account=get_object_or_404(account_details, pk=id)
    account.post_status=False
    account.save()
    return redirect('control')
    


