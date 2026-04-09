from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('write_blog/', views.write_blog, name='write_blog'),
    path('user_posts/', views.user_posts, name='user_posts'),
    path('all_posts/', views.all_posts, name='all_posts'),
]
