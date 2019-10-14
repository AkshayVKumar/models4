from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import *
# Create your views here.
def sample1(request):
    data={'data':'hello world'}
    return render(request,'sample1.html',context=data)

def sample2(request):
    objects=Topic.objects.qu()
    data={'objects':objects}
    return render(request,'sample2.html',context=data)

def sample3(request):
    objects=Access_Records.objects.query_set('date')
    data={'objects':objects}
    return render(request,'sample3.html',context=data)