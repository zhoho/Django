from django.shortcuts import render,HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('Welocome to my world')

def create(request):
    return HttpResponse('Create')

def read(request, id):
    return HttpResponse('Read' + id)
