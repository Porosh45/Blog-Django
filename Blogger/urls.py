from django.contrib import admin
from django.urls import path
from . import views
from .views import (PostListView, PostDetailView, PostDeleteView, UserPostListView, PostCreateView,
    PostUpdateView, CommentCreateView, LikeView)
urlpatterns = [
    path('',PostListView.as_view(), name = 'blog-home'),
    path('post/<int:pk>/',PostDetailView.as_view(), name = 'post-detail'),
    path('about/', views.about, name = 'blog-about'),
    #path('post/new/', PostCreateView.as_view(),name = 'post-create'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(), name = 'post-update'),
    path('post/new/',views.PostCreateView.as_view(), name = 'post-create'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(), name = 'post-delete'),
    path('user/<str:username>/',UserPostListView.as_view(), name = 'user-posts'),
    path('post/<int:pk>/comment/', CommentCreateView.as_view(), name = 'comment'),
    path('post/like-post/<int:pk>/', LikeView.as_view(), name = 'like'),
    path('post/like-save/', LikeView.as_view(), name = 'like-save'),
    path('post/like-delete/<int:pk>/', LikeView.as_view(), name = 'like-delete'),

]
