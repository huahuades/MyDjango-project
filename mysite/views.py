from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from stone.models import Stone

def check_login(fn):
    def wrap(request,*args,**kwargs):
        if 'username'not in request.session and 'uid' not in request.session:
            return HttpResponseRedirect('/users/login')

        return fn(request,*args,**kwargs)
    return wrap

def main(request):
    #dic={'username':'perl'}
    if request.session.get('username') and request.session.get('uid'):
        username=request.session.get('username')
        dic={'susername':username}
        return render(request,'main-yes.html',dic)
    return render(request,'mainno.html')

def map(requset):
    return render(requset,'map.html')
 
def mainno(request):
    return render (request,'mainno.html')

def text(request):
    return render(request,'text.html')

    
@check_login
def base(request):
    username=request.session['username']
    bic={'nusername':username}
    return render(request,'base.html',bic)


def introduce(request):
    username=request.session['username']
    bic={'nusername':username}
    return render(request,'introduce.html',bic)

@check_login
def price(request,pg):
    if pg==1:
        if request.method=='GET':
            username=request.session['username']
            bic={'nusername':username}
            stonetail=Stone.objects.all()
            return render(request,'001.html',bic)
        elif request.method=='POST':
            unitprice=float(request.POST['unitprice'])
            num=int(request.POST['num'])
            money=unitprice*num
            dic={'money':money}
            return render(request,'001.html',dic)
    elif pg==2:
        if request.method=='GET':
            username=request.session['username']
            bic={'nusername':username}
            return render(request,'002.html',bic)
        elif request.method=='POST':
            unitprice=float(request.POST['unitprice'])
            num=int(request.POST['num'])
            money=unitprice*num
            dic={'money':money}
            return render(request,'002.html',dic)
    elif pg==3:
        if request.method=='GET':
            username=request.session['username']
            bic={'nusername':username}
            return render(request,'003.html',bic)
        elif request.method=='POST':
            unitprice=float(request.POST['unitprice'])
            num=int(request.POST['num'])
            money=unitprice*num
            dic={'money':money}
            return render(request,'003.html',dic)
    elif pg==4:
        if request.method=='GET':
            username=request.session['username']
            bic={'nusername':username}
            return render(request,'004.html',bic)
        elif request.method=='POST':
            unitprice=float(request.POST['unitprice'])
            num=int(request.POST['num'])
            money=unitprice*num
            dic={'money':money}
            return render(request,'004.html',dic)
    elif pg==9:
        if request.method=='GET':
            username=request.session['username']
            bic={'nusername':username}
            return render(request,'009.html',bic)
        elif request.method=='POST':
            unitprice=float(request.POST['unitprice'])
            num=int(request.POST['num'])
            money=unitprice*num
            dic={'money':money}
            return render(request,'009.html',dic)
    elif pg==10:
        if request.method=='GET':
            username=request.session['username']
            bic={'nusername':username}
            return render(request,'010.html',bic)
        elif request.method=='POST':
            unitprice=float(request.POST['unitprice'])
            num=int(request.POST['num'])
            money=unitprice*num
            dic={'money':money}
            return render(request,'010.html',dic)
    elif pg==11:
        if request.method=='GET':
            username=request.session['username']
            bic={'nusername':username}
            return render(request,'011.html',bic)
        elif request.method=='POST':
            unitprice=float(request.POST['unitprice'])
            num=int(request.POST['num'])
            money=unitprice*num
            dic={'money':money}
            return render(request,'011.html',dic)
    elif pg==12:
        if request.method=='GET':
            username=request.session['username']
            bic={'nusername':username}
            return render(request,'012.html',bic)
        elif request.method=='POST':
            unitprice=float(request.POST['unitprice'])
            num=int(request.POST['num'])
            money=unitprice*num
            dic={'money':money}
            return render(request,'012.html',dic)
    elif pg==13:
        if request.method=='GET':
            username=request.session['username']
            bic={'nusername':username}
            return render(request,'013.html',bic)
        elif request.method=='POST':
            unitprice=float(request.POST['unitprice'])
            num=int(request.POST['num'])
            money=unitprice*num
            dic={'money':money}
            return render(request,'013.html',dic)
    elif pg==14:
        if request.method=='GET':
            username=request.session['username']
            bic={'nusername':username}
            return render(request,'014.html',bic)
        elif request.method=='POST':
            unitprice=float(request.POST['unitprice'])
            num=int(request.POST['num'])
            money=unitprice*num
            dic={'money':money}
            return render(request,'014.html',dic)
    elif pg==15:
        if request.method=='GET':
            username=request.session['username']
            bic={'nusername':username}
            return render(request,'015.html',bic)
        elif request.method=='POST':
            unitprice=float(request.POST['unitprice'])
            num=int(request.POST['num'])
            money=unitprice*num
            dic={'money':money}
            return render(request,'015.html',dic)

    elif pg==16:
        if request.method=='GET':
            username=request.session['username']
            bic={'nusername':username}
            return render(request,'016.html',bic)
        elif request.method=='POST':
            unitprice=float(request.POST['unitprice'])
            num=int(request.POST['num'])
            money=unitprice*num
            dic={'money':money}
            return render(request,'016.html',dic)
    elif pg==17:

        if request.method=='GET':
            username=request.session['username']
            bic={'nusername':username}
            return render(request,'017.html',bic)
        elif request.method=='POST':
            unitprice=float(request.POST['unitprice'])
            num=int(request.POST['num'])
            money=unitprice*num
            dic={'money':money}
            return render(request,'017.html',dic)
    elif pg==18:
        if request.method=='GET':
            username=request.session['username']
            bic={'nusername':username}
            return render(request,'018.html',bic)
        elif request.method=='POST':
            unitprice=float(request.POST['unitprice'])
            num=int(request.POST['num'])
            money=unitprice*num
            dic={'money':money}
            return render(request,'018.html',dic)
    elif pg==19:
        if request.method=='GET':
            username=request.session['username']
            bic={'nusername':username}
            return render(request,'019.html',bic)
        elif request.method=='POST':
            unitprice=float(request.POST['unitprice'])
            num=int(request.POST['num'])
            money=unitprice*num
            dic={'money':money}
            return render(request,'019.html',dic)
    elif pg==20:
        if request.method=='GET':
            username=request.session['username']
            bic={'nusername':username}
            return render(request,'020.html',bic)
        elif request.method=='POST':
            unitprice=float(request.POST['unitprice'])
            num=int(request.POST['num'])
            money=unitprice*num
            dic={'money':money}
            return render(request,'020.html',dic)

             
        
       

@check_login
def server_view(request):
    if request.method=='POST':
        cargo=request.POST['cargo']
        telephone=request.POST['telephone']
        truename=request.POST['truename']
    try:
        telephone=Usermessage.objects.create(telephone=telephone)
    except Exception as e:
        print('add user telephone error %s'%(e))
        return HttpResponse('您的请求我们已经收到，稍后工作人员会联系你！')

    #return HttpResponse('您的请求我们已经收到，稍后工作人员会联系你！')
        


    return HttpResponse(data)

def price_view(request,n,m):
    result=n*m
    return HttpResponse(result)

def sellshop(request):
    username=request.session['username']
    bic={'nusername':username}
    return render(request,'sellshop.html',bic)

def search(request):
    keyword=request.POST['keyword']
    if(keyword=='道牙石'):
        return HttpResponseRedirect('/price/1')
    elif(keyword=='路缘石'):
        return HttpResponseRedirect('/price/2')
    elif(keyword=='红砖'):
        return HttpResponseRedirect('/price/3')
    elif(keyword=='青砖'):
        return HttpResponseRedirect('/price/4')

    elif(keyword=='透水砖'):
        return HttpResponseRedirect('/price/9')
    elif(keyword=='面包砖'):
        return HttpResponseRedirect('/price/10')
    elif(keyword=='PC石'):
        return HttpResponseRedirect('/price/11')
    elif(keyword=='路沿石'):
        return HttpResponseRedirect('/price/12')
    elif(keyword=='路面砖'):
        return HttpResponseRedirect('/price/13')
    elif(keyword=='植草砖'):
        return HttpResponseRedirect('/price/14')
    elif(keyword=='红砖'):
        return HttpResponseRedirect('/price/15')
    elif(keyword=='树池路沿石'):
        return HttpResponseRedirect('/price/16')
    elif(keyword=='行道砖'):
        return HttpResponseRedirect('/price/17')
    else:
         return HttpResponse('请您输入正确的搜索物品！')
    

def error(request):
    return render(request,'error.html')


def communicate(request):
    username=request.session['username']
    bic={'nusername':username}
    return render(request,'communicate.html',bic)

def shop(requesrt,pg):
    if pg==1:
        return render(requesrt,'001.html')
    elif pg==2:
        return render(requesrt,'002.html')
    elif pg==3:
        return render(requesrt,'003.html')
    elif pg==4:
        return render(requesrt,'004.html')

    elif pg==9:
        return render(requesrt,'009.html')
    elif pg==10:
        return render(requesrt,'010.html')
    elif pg==11:
        return render(requesrt,'011.html')
    elif pg==12:
        return render(requesrt,'012.html')
    elif pg==13:
        return render(requesrt,'013.html')
    elif pg==14:
        return render(requesrt,'014.html')
    elif pg==15:
        return render(requesrt,'015.html')
    elif pg==16:
        return render(requesrt,'016.html')
    elif pg==17:
        return render(requesrt,'017.html')
    elif pg==18:
        return render(requesrt,'018.html')
    elif pg==19:
        return render(requesrt,'019.html')
    elif pg==20:
        return render(requesrt,'020.html')
    
    


