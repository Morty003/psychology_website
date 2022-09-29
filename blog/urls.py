from django.urls import path, include
from . import views


app_name = 'blog'

urlpatterns = [
    path('', views.PostListView.as_view(),  name='post_list_view'),
    path('<slug:posts_slug>/', views.PostDetailView.as_view(), name='single_post_view'),
 ]