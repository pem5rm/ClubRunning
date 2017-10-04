
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

# your imports, e.g. Django models

# import the relevant model
from myapp.models import RaceTime

#loop:
file = open("nircaData.csv", "r")
for line in file:
     line = line.strip().split(",")
     # add some custom validation\parsing for some of the fields

     raceTime = RaceTime(place = int(line[0]), firstName = line[1], lastName = line[2], team = line[3], time = line[4], session = line[5], event = line[6], date = line[7])
     try:
         raceTime.save()
     except:
         # if the're a problem anywhere, you wanna know about it
         print("there was a problem with line", line)