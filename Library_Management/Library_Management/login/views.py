from django.shortcuts import render
from django.http import HttpResponse
from django.core.serializers import serialize
from .models import UserDb
from django.views.decorators.http import require_http_methods

# Create your views here.

@require_http_methods(["GET", "POST", "PUT", "DELETE"])
def index_view(request):
    '''This is a simple view'''
    return render(request, 'index.html')

# APIs views

@require_http_methods(["GET", "POST", "PUT", "DELETE"])
def api_user_read():
    '''Api for read users'''
    users = UserDb.objects.all()
    users_json = serialize('json', users)
    return HttpResponse(users_json, content_type='text/json')
    
