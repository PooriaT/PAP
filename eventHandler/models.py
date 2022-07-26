from django.db import models
import datetime


# Create your models here.

class Conference(models.Model):
    conferenceID = models.AutoField(primary_key=True)
    conferenceName = models.CharField(max_length=150)
    conferenceOrganizer = models.CharField(max_length=30)
    city = models.CharField(max_length=20)
    dateRange = models.DurationField(default=datetime.timedelta(days=1), blank=True)

class Event(models.Model):
    eventID = models.IntegerField(unique=True)
    eventName = models.CharField(max_length=150)
    eventLocation = models.CharField(max_length=20)
    eventRoom = models.CharField(max_length=15)
    eventDate = models.DateTimeField()
    eventSpeaker = models.CharField(max_length=60)
    conference = models.ForeignKey('Conference', on_delete=models.CASCADE, blank=True)
    
     

