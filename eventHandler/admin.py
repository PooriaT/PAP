from django.contrib import admin

# Register your models here.
from .models import Conference
from .models import Event
# Register your models here.

admin.site.register(Conference)
admin.site.register(Event)