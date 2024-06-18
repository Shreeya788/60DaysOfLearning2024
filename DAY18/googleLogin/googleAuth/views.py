from django.shortcuts import render
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.template import loader

def home(request):
    return render(request,'home.html')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')