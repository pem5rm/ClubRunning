#Script 1:
from myapp.models import RaceTime
file = open("nircaData.csv", "r")
for line in file:
    line = line.strip().split(";")
    raceTime = RaceTime(place = int(line[0]), firstName = line[1], lastName = line[2], team = line[3], time = line[4], session = line[5], event = line[6], meet = line[7], date = line[8], score = line[9], bib = line[10], location = line[11], host = line[12], gender = line[13])
    raceTime.save()



#Script 2:

from myapp.models import RaceTime
file = open("nircaData.csv", "r")
for line in file:
    line = line.strip().split(",")
    raceTime = RaceTime(place = int(line[0]), firstName = line[1], lastName = line[2], team = line[3], time = line[4], session = line[5], event = line[6], meet = line[7], date = line[8])
    raceTime.save()

#Deletion Script:
RaceTime.objects.filter(someField="something").delete()

RaceTime.objects.filter(meet="UB Bulls XC Invite", date="2015-10-10 00:00:00").delete()

RaceTime.objects.filter(meet="NIRCA XC National Championship", date="2015-11-14 00:00:00").delete()

#Save Backup Script
from myapp.models import RaceTime
file = open("output.txt", "a")
times = RaceTime.objects.filter(meet="JMU Invitational")
for time in times:
    file.write(str(time.place).strip() + "," + time.firstName.strip() + "," + time.lastName.strip() + "," + time.team.strip() + "," + time.time.strip() + "," + time.session.strip() + "," + time.event.strip() + "," + time.meet.strip() + "," + str(time.date).strip() + "," + str(time.score.strip()) + "," + str(time.bib.strip()) + "," + time.location.strip() + "," + time.host.strip() + "," + time.gender.strip() + "\n")
file.close()

#Get all athletes


#fix
from myapp.models import RaceTime
RaceTime.objects.filter(meet="NIRCA XC National Championship",session = "FR/SO Race").delete()

#assign sessionOrder
from myapp.models import RaceTime
results = RaceTime.objects.filter(meet="NIRCA XC National Championship",session = "B Race")
for result in results:
    result.sessionOrder = 1
    result.save()




from myapp.models import RaceTime
results = RaceTime.objects.filter(meet="Mid-Atlantic Regional")
for result in results:
    result.meet = "Mid-Atlantic Regional"
    result.save()



from myapp.models import RaceTime
RaceTime.objects.filter(meet="Great Plains Regional", gender="Male").delete()


from myapp.models import RaceTime
results = RaceTime.objects.filter(meet="Mid-Atlantic Regional")
print(len(results))


#Get list of all teams
from myapp.models import RaceTime
results = RaceTime.objects.all()
teams = []
for r in results:
    if r.team not in teams:
        teams.append(r.team)
print(teams)

#Fix names
from myapp.models import RaceTime
results = RaceTime.objects.all()
for r in results:
    if r.firstName == "Brandon" and r.lastName == "Kannewurff" and r.team == "University of Virginia von":
        r.firstName = "Brandon"
        r.lastName = "von Kannewurff"
        r.team = "University of Virginia"
        r.save()
    elif r.firstName == "Bella" and r.lastName == "Heyde" and r.team == "University of Virginia Vice-Van":
        r.firstName = "Bella"
        r.lastName = "Vice-Van Heyde"
        r.team = "University of Virginia"
        r.save()
    elif r.firstName == "Lee" and r.lastName == "Mary" and r.team == "Duke University Lawrence":
    # elif r.firstName == "Mary Lee" and r.team == "Duke University":
        r.firstName = "Mary Lee"
        r.lastName = "Lawrence"
        r.team = "Duke University"
        r.save()
    elif r.firstName == "Anna" and r.lastName == "Mary" and r.team == "University of Virginia Adams":
        r.firstName = "Mary Anna"
        r.lastName = "Adams"
        r.team = "University of Virginia"
        r.save()
    elif r.firstName == "Mary" and r.lastName == "Pierce" and r.team == "University of North Carolina Gates":
        r.firstName = "Mary"
        r.lastName = "Gates Pierce"
        r.team = "University of North Carolina"
        r.save()



#Fix () scores
from myapp.models import RaceTime
results = RaceTime.objects.all()
for r in results:
    if ("(" in r.team) and (")" in r.team):
        s = r.team.strip("(").split(")")
        r.score = "(" + s[0] + ")"
        r.team = s[1].strip()
        r.save()

