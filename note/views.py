from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Note

def check_login(fn):
    def wrap(request,*args,**kwargs):
        if 'username'not in request.session and 'uid' not in request.session:
            return HttpResponseRedirect('/users/login')

        return fn(request,*args,**kwargs)
    return wrap
# Create your views here.

@check_login
def index(request):
    if request.method=='GET':
        username=request.session['username']
        bic={'nusername':username}
        return render(request,'note.html',bic)
    elif request.method=='POST':
        uid=request.session['uid']
        title=request.POST['title']
        content=request.POST['content']
        Note.objects.create(title=title,content=content,usermessage_id=uid)
        return HttpResponse('您的意见我们收到啦,感谢反馈！')