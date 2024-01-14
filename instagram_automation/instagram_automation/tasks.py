from celery import Celery
from insta_bot.functions import follow,login,unfollow,postpicture
app = Celery('instagram_automation')

app = Celery('tasks', broker='pyamqp://guest@localhost//')

@app.task
def clogin(username,password):
    login(username,password)
    
@app.task
def cfollow(username):
    follow(username)

@app.task
def cunfollow(username):
    unfollow(username)

@app.task
def cpostpicture(caption,imagelink):
    postpicture(imagelink,caption)
