from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views import generic

def index(request):
    return HttpResponse('Hello, This is the first page')
# Create your views here.

def myview(request):
    if request.method == "GET":
        # to get or delete items from models
        pass
    if request.method == "POST":
        # to insert or update items from models
        pass

def myview2(request): 
    if request.method=='GET': 
        val = request.GET['key'] 
        #perform read or delete operation on the model 
    if request.method=='POST': 
        val = request.POST['key'] 
        #perform insert or update operation on the model 

def myview3(request):  

      if request.method=='GET':  
            #perform read or delete operation on the model  
            pass
      if request.method=='POST':  
            #perform insert or update operation on the model  
            context={ } #dict containing data to be sent to the client  

      return render(request, 'mytemplate.html', context) 

class home(View):
    def get(self, request):
        return HttpResponse('response to GET request')

    def post(self, request):
        return HttpResponse('response to POST request')
    
# Generic views
# Django makes the view declaration process still easier with its generic class-based views. The django.views.generic module contains several view classes that provide the functionality required to perform tasks such as rendering a template, showing an instance, showing the list of instances, adding a new model instance, updating an instance and so on. 

# Some generic views are TemplateView, CreateView, ListView, DetailView, UpdateView to name a few.

# You need to subclass the generic view and set the properties like model and template_name. Django will internally perform all the heavy lifting which you had to do by yourself in a function-based view.