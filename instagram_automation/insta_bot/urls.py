from django.urls import path
from . import views

urlpatterns=[
    path('home',views.index,name='home'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),  # Add this line for logout
    path('accounts', views.accounts, name='accounts'),
    path('control', views.control, name='control'),
    path('addaccount', views.addaccount, name='addaccount'),
    path('accountsetup/<int:account_id>', views.accountsetup, name='accountsetup'),
    path('addfollowaccount', views.addfollowaccount, name='addfollowaccount'),
    path('add_directorylink', views.add_directorylink, name='add_directorylink'),
    path('deletefollowaccount/<int:account_id>', views.delete_followaccount, name='deletefollowaccount'),  # Add this line for deleting follow accounts
    path('activatefollow/<int:account_id>', views.activate_follow, name='activatefollow'),  # Add this line for activating follow
    path('deactivatefollow/<int:account_id>', views.deactivate_follow, name='deactivatefollow'),  # Add this line for deactivating follow
    path('activateunfollow/<int:account_id>', views.activate_unfollow, name='activateunfollow'),  # Add this line for activating unfollow
    path('deactivateunfollow/<int:account_id>', views.deactivate_unfollow, name='deactivateunfollow'),  # Add this line for deactivating unfollow
    path('activatepost/<int:account_id>', views.activate_post, name='activatepost'),  # Add this line for activating post
    path('deactivatepost/<int:account_id>', views.deactivate_post, name='deactivatepost'),
    path('', views.redirect_to_home),
    path('change_link',views.change_link,name='change_link'),
    
    path('testf', views.testf, name='testf'),  # Add this line for testf
]
    
    

    

    
      

    
    
    

    
    
    
    
