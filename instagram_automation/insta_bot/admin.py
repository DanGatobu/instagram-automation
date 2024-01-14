from django.contrib import admin
from .models import account_details,follow_accounts,directory_links,monitor_follow

# Register your models here.

admin.site.register(account_details)
admin.site.register(follow_accounts)
admin.site.register(directory_links)
admin.site.register(monitor_follow)



