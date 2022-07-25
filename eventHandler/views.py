from django.shortcuts import render
from django.template import loader

from django.http import HttpResponse

from .models import Userprofile
from .models import Conference
from .models import Event

#Index Page
def index(request):  
    allEvents = Event.objects.all()
    allConf = Conference.objects.all()
   
            
    template = loader.get_template('eventHandler/index.html')
    context = {
        'conferences' : allConf,
        'events': allEvents,
    }
    return HttpResponse(template.render(context, request))


#Login Page
def login(request):
    pass

#Register Page
def register(request):
    pass