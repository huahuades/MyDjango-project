from django.urls import path
from .import views

urlpatterns=[
    path('sign/',views.sign),
    path('login/',views.login),
    path('consign',views.consign),
    path('conlogin',views.conlogin),
    path('logout',views.logout)
]
