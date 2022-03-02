from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import Usermessage
import hashlib
# Create your views here.
def sign(request):
    return render(request,'sign.html')

def login(request):
    return render(request,'login.html')

def consign(request):
    if request.method=='GET':
        return render(request,'login.html')
    elif request.method=='POST':
        #要判断一下两次输入的密码是否一样
        #还要判断一下数据库中是否已经有这个人
        username=request.POST['username']
        password=request.POST['password']
        conpassword=request.POST['conpassword']
        if password!=conpassword:
            dic={'data2':'两次密码输入的不一致'}
            return render(request,'sign.html',dic)
        old_username=Usermessage.objects.filter(username=username)
        if old_username:
            dic={'data1':'此用户名已被注册'}
            return render(request,'sign.html',dic)
        m=hashlib.md5()
        m.update(password.encode())
        safepassword=m.hexdigest()
        #避免并发写入问题：
        try:
            user=Usermessage.objects.create(username=username,password=safepassword)
        except Exception as e:
            print('create user error %s'%(e))
            dic={'data3':'此用户名已被注册'}
            return render(request,'sign.html',dic)
        
        #免登录一天
        request.session['username']=username
        request.session['uid']=user.id

        dic={'susername':username}
        #return render(request,'main-yes.html',dic)
        return HttpResponseRedirect('/main',dic)

def conlogin(request):
    if request.method=='GET':
        #检查session中是否有数据，现在的session中存储的数据为14天，也就是说14天免登陆
        if request.session.get('username')and request.session.get('uid'):
            return HttpResponse('已登陆')
            #dic={'ausername':username}
            #return render(request,'main.html',dic)
        #若session中没有数据，cookies中也肯定没有，不做判断
        return render(request,'login.html')
    elif(request.method=='POST'):
        username=request.POST['username']
        password=request.POST['password']
        #如果数据库中没有username则提示先去注册
        #如果数据库中有返回主页面
        try:
            user=Usermessage.objects.get(username=username)
        except Exception as e:
            dic={'data4':'若没有注册，请先注册，若已经注册，用户名或密码有问题'}
            return render(request,'login.html',dic)
        p=hashlib.md5()
        p.update(password.encode())
        #safep=p.hexdigest()
        if p.hexdigest()!=user.password:
            dic={'data5':'您的用户名或密码有问题！'}
            return render(request,'login.html',dic)

        #return render(request,'main.html')
        #记录会话状态
        request.session['username']=username
        request.session['uid']=user.id
        dic={'lusername':username}
        #resp=render(request,'main-yes.html',dic)
        resp= HttpResponseRedirect('/main','dic')
        #判断用户是否点击了remember
        if 'remember' in request.POST:
            resp.set_cookie('username',username,3600*24*3)
            resp.set_cookie('uid',user.id,3600*24*3)
        return resp


def logout(request):
    #删除session
    if 'username' in request.session:
        del request.session['username']
    if 'uid'in request.session:
        del request.session['uid']

    #删除cookies
    resp= HttpResponseRedirect('/main')
    if 'username'in request.COOKIES:
        resp.delete_cookie('username')
    if 'uid'in request.COOKIES:
        resp.delete_cookie('uid')
    return resp
