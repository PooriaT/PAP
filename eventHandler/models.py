from django.db import models
import datetime


# Create your models here.
class Userprofile(models.Model):
    userID = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30, unique=True)
    fname = models.CharField(max_length=20) #Firstname
    lname = models.CharField(max_length=30) #Lastname
    email = models.EmailField(unique=True)
    #privilege = models.IntegerField() # 0 -> admin, 1 -> conference organizer, 2 -> speaker, 3-> attendee
    password = models.CharField(max_length=20)

class Conference(models.Model):
    conferenceID = models.AutoField(primary_key=True)
    conferenceName = models.CharField(max_length=60)
    conferenceOrganizer = models.CharField(max_length=30)
    city = models.CharField(max_length=20)
    dateRange = models.DurationField(default=datetime.timedelta(days=1), blank=True)
    events = models.ForeignKey('Event', on_delete=models.CASCADE)

class Event(models.Model):
    eventID = models.IntegerField(unique=True)
    eventName = models.CharField(max_length=20)
    eventLocation = models.CharField(max_length=20)
    eventRoom = models.CharField(max_length=15)
    eventDate = models.DateTimeField()
    eventSpeaker = models.CharField(max_length=60)
    
     

