#Django
from django.http import HttpResponse

from django.shortcuts import render

def list_p(request):
    return render(request,'feed.html',{'name':'angel'})
# Create your views here.
