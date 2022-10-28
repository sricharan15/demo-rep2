from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.
def home(request):
    return HTTPResponse('sdgfjdsgfh</h1>')
def add(request):
    return render(request,'results.html',{'name':'add'})