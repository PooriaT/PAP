from django.shortcuts import render, redirect
from django.template import loader

from django.http import HttpResponse

from django.contrib.auth import authenticate, login, logout


from .models import Conference
from .models import Event

#Index Page
def index(request):  
    allConf = Conference.objects.all()
    
    print(request.user)
    if request.user.is_authenticated:
        allEvents = Event.objects.all()
    else:
        allEvents = {}
    template = loader.get_template('eventHandler/index.html')
    context = {
        'conferences' : allConf,
        'events': allEvents,
    }
    return HttpResponse(template.render(context, request))


#Login Page
def loginFunc(request):
    print(request.POST)
    if request.POST:
        print(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            pass
    template = loader.get_template('eventHandler/login.html')
    context = {
        'events': {},
    }
    return HttpResponse(template.render(context, request))


#Register Page
def register(request):
    pass