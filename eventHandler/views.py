from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse



from django.contrib.auth import authenticate, login, logout


from .models import Conference
from .models import Event

#Index Page
def index(request):  
    allConf = Conference.objects.all()
    
    user_fname = ', Guest'
    login_stat = True
    if request.user.is_authenticated:
        allEvents = Event.objects.all()
        user_fname = ', ' + request.user.get_short_name()
        login_stat = False
    else:
        allEvents = {}
    template = loader.get_template('eventHandler/index.html')
    context = {
        'loginStat' : login_stat,
        'name' : user_fname,
        'conferences' : allConf,
        'events': allEvents,
    }
    return HttpResponse(template.render(context, request))


#Login Page
def loginFunc(request):
    message = ""
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
            message = "Invalid Username or Password!!!"
    
    template = loader.get_template('eventHandler/login.html')
    context = {
        'message': message,
    }
    return HttpResponse(template.render(context, request))


def logoutFunc(request):
    logout(request)
    # Redirect to a success page.
    return redirect('index')

#Register Page
def register(request):
    pass