from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from . models import Stone

# Create your views here.
def stoneindex(request):
    return render(request,'stoneindex.html')

def stonedetail(request):

    stonedetail=Stone.objects.all()
    return render(request,'stonedetail.html',locals())