from django.contrib import admin
from .models import Post, Comment, Contributor
from django_summernote.admin import SummernoteModelAdmin

# Customize the admin interface for the Contributor model
@admin.register(Contributor)
class ContributorAdmin(SummernoteModelAdmin):
    list_display = ('name',)

# Customize the admin interface for the Post model
# Use the Summernote editor for the content field
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    summernote_fields = ('content',)

# Customize the admin interface for the Comment model
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


# Register your models here.
