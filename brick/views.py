from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Brick

# Create your views here.
def brickindex(request):
    return render(request,'brickindex.html')

def brickdetail(request):
    brickdetail=Brick.objects.all()
    return render(request,'brickdetail.html',locals())