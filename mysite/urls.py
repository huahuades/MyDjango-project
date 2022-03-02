"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .import views


urlpatterns = [
    path('/',views.main,name="index"),
    path('map',views.map),
    path('admin/', admin.site.urls),
    #path('mainno',views.mainno),
    path('main-yes',views.main,name="index"),
    path('main',views.main,name="index"),
    path('base.html',views.base),
    path('stone/',include('stone.urls')),
    path('brick/',include('brick.urls')),
    path('note/',include('note.urls')),
    path('shoppingcart/',include('shoppingcart.urls')),
    path('users/',include('users.urls')),
    path('price/<int:pg>',views.price,name='price'),
    path('introduce',views.introduce,name='introduce'),
    path('search',views.search,name='search'),
    path('communicate',views.communicate),
    path('sellshop.html',views.sellshop,name="sellshop"),
    path('server',views.server_view),
    path('text',views.text),
    path('<int:n>/<int:m>',views.price_view)
]
