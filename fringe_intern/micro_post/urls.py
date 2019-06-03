from django.urls import path
from micro_post import views

app_name = 'api'
urlpatterns = [
    # 書籍
    path('v1/posts/', views.post_list, name='post_list'),
    path('v1/posts/create', views.post_create, name='post_create'),
    path('v1/posts/<str:post_id>/comments/create', views.comment_create, name='comment_create'),
    path('v1/posts/<str:post_id>/comments', views.comment_list, name='comment_list'),
]
