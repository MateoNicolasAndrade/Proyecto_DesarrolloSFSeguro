from django.shortcuts import render
from django.http import HttpResponse
from django.core.serializers import serialize
from .models import UserDb

# Create your views here.

def indexView(request):
    '''This is a simple view'''
    return render(request, 'index.html')

# APIs views

def ApiUserRead(request):
    '''Api for read users'''
    users = UserDb.objects.all()
    users_json = serialize('json', users)
    return HttpResponse(users_json, content_type='text/json')
    
