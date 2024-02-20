from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.

def indexView(request):
    '''This is a simple view'''
    return render(request, 'index.html')
