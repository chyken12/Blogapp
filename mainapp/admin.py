from django.contrib import admin

# Register your models here.
from .models import Post,Subscribers,Newsletter

admin.site.register(Post)
admin.site.register(Subscribers)
admin.site.register(Newsletter)
