
from django.urls import path
from . import views



urlpatterns = [

    path('', views.home, name='home'),
    path('register/', views.Register, name='register'),
    path('login/', views.Login, name='login'),
    path('blogs/', views.blogs, name='blogs'),
    path('add_blogs/', views.add_blogs, name='add_blogs'),
    path('logout/', views.user_logout, name='logout'),
    path('delete_blog/<str:desc>/', views.delete_blog, name='delete_blog'),
     path('blog/<str:desc>/', views.view_blog, name='view_blog'),
    path('blog/<str:desc>/comment/', views.add_comment, name='add_comment'),
    path('myblogs/', views.my_blogs, name='my_blogs'),

]

