from . import views
from django.urls import path
from django.contrib import admin
# from blog.views import AboutUs  --- commented this out as it's gone from view

# URL patterns for blog app
urlpatterns = [
    path('aboutus/', views.AboutUs.as_view(), name='aboutus'),
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('create/post', views.AddPost.as_view(), name='post_form'),
    path('<slug:slug>/update/', views.UpdatePost.as_view(), name='update_post'),
    path('<slug:slug>/delete/', views.PostDelete.as_view(), name='post_delete'),
]
