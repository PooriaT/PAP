from django.shortcuts import render
from django.template import loader

from django.http import HttpResponse

from .models import Userprofile
from .models import Conference
from .models import Event


def index(request):  
    template = loader.get_template('eventHandler/index.html')
    # context = {
    #     'latest_question_list': latest_question_list,
    # }
    context = {}
    return HttpResponse(template.render(context, request))


