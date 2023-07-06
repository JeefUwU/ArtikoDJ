from django.urls import path
from .views import index, screen1,user,SignUp,login_user
from . import views

urlpatterns=[
    path('', index, name="index"),
    path('screen1', screen1, name="screen1"),
    path('Perfil', user, name="user"),
    path('Perfil/<str:username>/', views.user, name='user'),
    path('SignUp', SignUp, name="SignUp"),
    path('login_user', login_user, name="login_user"),
    path('Post/', views.post, name='post'),
    
    path('shop', views.shop, name='shop'),
    path('crud', views.crud, name='crud'),
    path('carrito', views.carrito, name='carrito'),
]