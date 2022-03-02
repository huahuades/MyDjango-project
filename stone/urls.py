from django.urls import path
from .import views
urlpatterns = [
    path('index/',views.stoneindex),
    path('all_stone/',views.stonedetail)
]