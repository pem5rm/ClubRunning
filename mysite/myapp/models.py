# import os
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
# # Uncomment below for Django 1.7 +
#
# from django.core.exceptions import AppRegistryNotReady
# try:
#     from django.apps import apps
#     apps.check_apps_ready()
#     print("success")
# except AppRegistryNotReady:
#     import django
#     django.setup()
#     print("failure")

from django.db import models

# Create your models here.

# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')
#
#
# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
class RaceTime(models.Model):
    place = models.IntegerField(default=0)
    firstName = models.CharField(max_length=50, default="N/A")
    lastName = models.CharField(max_length=50, default="N/A")
    team = models.CharField(max_length=100, default="N/A")
    time = models.CharField(max_length=25, default="N/A")
    session = models.CharField(max_length=25, default="N/A")
    event = models.CharField(max_length=50, default="N/A")
    meet = models.CharField(max_length=100, default="N/A")
    date = models.DateTimeField( ['%Y-%m-%d %H:%M:%S'], default='2000-01-01 00:00:00' )
    score = models.CharField(max_length=25, default="N/A")
    bib = models.CharField(max_length=25, default="N/A")
    location = models.CharField(max_length=150, default="N/A")
    host = models.CharField(max_length=150, default="N/A")
    gender = models.CharField(max_length=20, default="N/A")
    sessionOrder = models.IntegerField(default=0)


    def __str__(self):
        return str(self.date) + " , " + self.meet + " , " + self.firstName + " " + self.lastName + " , " + self.time + " , " + self.event + " , " + self.team + " , " + self.session



#loop:


#Working shell code:
# """
# from myapp.models import RaceTime
# file = open("nircaData.csv", "r")
# for line in file:
#     line = line.strip().split(",")
#     raceTime = RaceTime(place = int(line[0]), firstName = line[1], lastName = line[2], team = line[3], time = line[4], session = line[5], event = line[6])
#     raceTime.save()

#"""



    # except:
    #     # if the're a problem anywhere, you wanna know about it
    #     print("there was a problem with line", line)