from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Cart


def check_login(fn):
    def wrap(request,*args,**kwargs):
        if 'username'not in request.session and 'uid' not in request.session:
            return HttpResponseRedirect('/users/login')

        return fn(request,*args,**kwargs)
    return wrap
# Create your views here.

@check_login
def shoppingcartindex(request):
    uid=request.session['uid']

    
    cartdetail=Cart.objects.filter(is_active=True)
    return render(request,'shoppingcartindex.html',locals())

def deleteshop(request,shop_id):
    
    shop=Cart.objects.get(id=shop_id,is_active=True)
    shop.is_active=False
    shop.save()
    return HttpResponseRedirect('/shoppingcart/index')



def shoppingcartadd(request,pg):
    if(pg==1):
        return render(request,'shoppingcartadd1.html')
    elif(pg==2):
        return render(request,'shoppingcartadd2.html')
    elif(pg==3):
        return render(request,'shoppingcartadd3.html')
    elif(pg==4):
        return render(request,'shoppingcartadd4.html')
    elif(pg==4):
        return render(request,'shoppingcartadd4.html')
    elif(pg==4):
        return render(request,'shoppingcartadd4.html')
    elif(pg==9):
        return render(request,'shoppingcartadd9.html')
    elif(pg==10):
        return render(request,'shoppingcartadd10.html')
    elif(pg==11):
        return render(request,'shoppingcartadd11.html')
    elif(pg==12):
        return render(request,'shoppingcartadd12.html')
    elif(pg==13):
        return render(request,'shoppingcartadd13.html')
    elif(pg==14):
        return render(request,'shoppingcartadd14.html')
    elif(pg==15):
        return render(request,'shoppingcartadd15.html')
    elif(pg==16):
        return render(request,'shoppingcartadd16.html')
    elif(pg==17):
        return render(request,'shoppingcartadd17.html')
    elif(pg==18):
        return render(request,'shoppingcartadd18.html')
    elif(pg==19):
        return render(request,'shoppingcartadd19.html')
    elif(pg==20):
        return render(request,'shoppingcartadd20.html')
    
   
@check_login
def addshop(request):
   # for shopname in request.POST.getlist('shopname'):
          #if not shopname:
               #continue
    #list_item.shopname = Cart(shopname)
    #list_item.save()
    
    uid=request.session['uid']
    num=request.POST['quantity']
    size=request.POST['shopsize']
    name=request.POST['shopname']
    unitprice=request.POST['unitprice']
    Cart.objects.create(shopname=name,shopsize=size,shopprice=unitprice,shopquantity=num,usermessage_id=uid)
    #return render(request,'shoppingcartindex.html',locals())
    return HttpResponseRedirect('/shoppingcart/index')


