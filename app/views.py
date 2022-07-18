from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.forms import *


def validating(request):
    NF=NameForm()
    d={'NF':NF}

    if request.method=='POST':
        FD=NameForm(request.POST)
        if FD.is_valid():
            return HttpResponse('Valid Form')
    return render(request,'validating.html',d)