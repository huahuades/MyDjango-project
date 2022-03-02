from django.urls import path
from .import views
urlpatterns = [
    path('index/',views.brickindex),
    path('all_brick/',views.brickdetail)
]