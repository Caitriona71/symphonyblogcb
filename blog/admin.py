from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
admin.site.register(Post)
