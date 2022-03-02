from django.urls import path
from .import views

urlpatterns=[
    path('index/',views.shoppingcartindex),
    path('addshop/<int:pg>',views.shoppingcartadd),
    path('add',views.addshop),
    path('delete/<int:shop_id>',views.deleteshop)
]