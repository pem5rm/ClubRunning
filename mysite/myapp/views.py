#TO DO:
# Mid-Atlantic Regional not working


from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.db.models import Q
import string

from .models import RaceTime
import operator, functools

CURRENT_YEAR = "2016"

class IndexView(generic.ListView):
    template_name = 'myapp/index.html'


    def get_queryset(self):
        return None



    def get_context_data(self, *args, **kwargs):
        context = super(generic.ListView, self).get_context_data(*args, **kwargs)

        mens_results = RaceTime.objects.all().filter(event="8K", gender="Male", date__year=CURRENT_YEAR).order_by("time")
        womens_results = RaceTime.objects.all().filter(event="6K", gender="Female", date__year=CURRENT_YEAR).order_by("time")

        # reversed = False
        # orderBy = 0
        # orderDict = {"rank" : 0, "name" : 1, "time" : 2, "meet" : 3}
        # order = self.request.GET.get('order_by')
        # if order:
        #     order = order.split("_")
        #     orderBy = orderDict[order[0]]
        #     if order[0] == "up":
        #         reversed = True


        ranks = []
        names = []
        times = []
        meets = []
        teams = []


        r = 1
        for i in range(len(mens_results)):
            if (len(mens_results[i].time) <= 8 and mens_results[i].firstName + " " + mens_results[i].lastName  not in names):
                ranks.append(r)
                r+=1
                names.append(mens_results[i].firstName + " " + mens_results[i].lastName)
                times.append(mens_results[i].time)
                meets.append(mens_results[i].meet)
                teams.append(mens_results[i].team)




        final_mens_results = [[], [], [], [], []]

        for i in range(100):
            final_mens_results[0].append(ranks[i])
            final_mens_results[1].append(names[i])
            final_mens_results[2].append(times[i])
            final_mens_results[3].append(meets[i])
            final_mens_results[4].append(teams[i])


        ranks = []
        names = []
        times = []
        meets = []
        teams = []

        r = 1
        for i in range(len(womens_results)):
            if (len(womens_results[i].time) <= 8 and womens_results[i].firstName + " " + womens_results[i].lastName  not in names):
                ranks.append(r)
                r+=1
                names.append(womens_results[i].firstName + " " + womens_results[i].lastName)
                times.append(womens_results[i].time)
                meets.append(womens_results[i].meet)
                teams.append(womens_results[i].team)


        final_womens_results = [[], [], [], [], []]

        for i in range(100):
            final_womens_results[0].append(ranks[i])
            final_womens_results[1].append(names[i])
            final_womens_results[2].append(times[i])
            final_womens_results[3].append(meets[i])
            final_womens_results[4].append(teams[i])





        context["zipped_mens_8k"] = sorted(zip(final_mens_results[0], final_mens_results[1], final_mens_results[2], final_mens_results[3], final_mens_results[4]), key=lambda x: x[0], reverse=False)
        context["zipped_womens_6k"] = sorted(zip(final_womens_results[0], final_womens_results[1], final_womens_results[2], final_womens_results[3], final_womens_results[4]), key=lambda x: x[0], reverse=False)
        context["current_year"] = CURRENT_YEAR



        return context



# need to do fix for names with spaces, similarly as was done in athleteView
class ResultsView(generic.ListView):
    template_name = 'myapp/results.html'
    context_object_name = 'result_list'

    def get_queryset(self):
        result = RaceTime.objects.all()
        query = self.request.GET.get('q')

        try:
            query_list = query.split()

            if query:

                for i in range(len(query_list)):
                    query_list[i] = query_list[i].lower()
                    query_list[i] = ''.join(word[0].upper() + word[1:] for word in query_list[i].split())



                result = result.filter(firstName__in = query_list) | result.filter(lastName__in = query_list)



                #Prioritizes: correct first and last; then correct but wrong order; then just last name
                r1 = []
                r2 = []
                r3 = []
                r4 = []

                # search names
                if len(query_list) > 1:
                    for r in result:

                        if r.firstName == query_list[0] and r.lastName == query_list[1]:
                            r1.append(r.firstName + " " + r.lastName + " (" + r.team + ")")

                        elif r.firstName == query_list[1] and r.lastName == query_list[0]:
                            r2.append(r.firstName + " " + r.lastName + " (" + r.team + ")")

                        elif r.lastName in query_list:
                            r3.append(r.firstName + " " + r.lastName + " (" + r.team + ")")

                        else:
                            r4.append(r.firstName + " " + r.lastName + " (" + r.team + ")")
                else:
                    for r in result:
                        if r.lastName in query_list:
                            r3.append(r.firstName + " " + r.lastName + " (" + r.team + ")")
                        else:
                            r4.append(r.firstName + " " + r.lastName + " (" + r.team + ")")

                # search meets



                result2 = r1 + r2 + r3 + r4
                result = []
                for r in result2:
                    if r not in result:
                        result.append(r)

        except:
            pass

        return(result)

class AthleteView(generic.ListView):
    template_name = 'myapp/athlete.html'
    context_object_name = 'athlete_list'

    # Not currently used
    def get_queryset(self):

        athleteData = str(self.kwargs['name']).replace(';', '').replace("(", "").replace(")", "").replace('  ', ' ').split(" ")

        athleteFirst = athleteData[0]
        athleteLast = athleteData[1]
        athleteSchool = " ".join((athleteData[2:]))
        results = RaceTime.objects.all().filter(firstName=athleteFirst, lastName=athleteLast, team=athleteSchool)

        # displayInfo = {"time":[], "meet":[], "date":[], "place": [], "round": []}
        # for athlete in results:
        #     displayInfo.append()
        return (results)


    def get_context_data(self, *args, **kwargs):
        context = super(generic.ListView, self).get_context_data(*args, **kwargs)
        athleteData = str(self.kwargs['name']).replace(';', '').replace('  ', ' ').replace(")", "").split("(")

        # To deal with spaces in names, this assumes by default that the space is in the last name
        athleteName = athleteData[0].split()
        athleteFirst = athleteName[0]
        athleteLast = " ".join(athleteName[1:])
        athleteSchool = " ".join((athleteData[1:]))

        # Hard coded exceptions for when the space is actually in the first name; code only runs if there is a space in last name, so it should have minimal impact on performance
        if " " in athleteLast:
            if athleteLast == "Lee Lawrence" and athleteSchool == "Duke University":
                athleteFirst = "Mary Lee"
                athleteLast = "Lawrence"

        results = RaceTime.objects.all().filter(firstName=athleteFirst, lastName=athleteLast, team=athleteSchool)

        context["athlete_name"] = athleteFirst + " " + athleteLast
        context["athlete_school"] = athleteSchool

        events = []
        times = []
        meets = []
        dates = []
        places = []
        sessions = []

        for result in results:
            events.append(result.event)
            times.append(result.time)
            meets.append(result.meet)
            dates.append(result.date)
            places.append(result.place)
            sessions.append(result.session)


        # times(0), meets(1), dates(2), places(3), sessions(4)
        fiveK_results = [[], [], [], [], []]
        sixK_results = [[], [], [], [], []]
        eightK_results = [[], [], [], [], []]

        for i in range(len(events)):
            if events[i] == "5K":
                fiveK_results[0].append(times[i])
                fiveK_results[1].append(meets[i])
                fiveK_results[2].append(dates[i])
                fiveK_results[3].append(places[i])
                fiveK_results[4].append(sessions[i])

            elif events[i] == "6K":
                sixK_results[0].append(times[i])
                sixK_results[1].append(meets[i])
                sixK_results[2].append(dates[i])
                sixK_results[3].append(places[i])
                sixK_results[4].append(sessions[i])

            elif events[i] == "8K":
                eightK_results[0].append(times[i])
                eightK_results[1].append(meets[i])
                eightK_results[2].append(dates[i])
                eightK_results[3].append(places[i])
                eightK_results[4].append(sessions[i])


        # context["time"] = times
        # context["meet"] = meets
        # context["date"] = dates
        # context["places"] = places
        # context["rounds"] = rounds


        # times(0), meets(1), dates(2), places(3), sessions(4)


        if fiveK_results != [[], [], [], [], []]:
            context["zipped_5k_results"] = sorted(zip(fiveK_results[0], fiveK_results[1], fiveK_results[2], fiveK_results[3], fiveK_results[4]), key=lambda x: x[2], reverse=True)

        if sixK_results != [[], [], [], [], []]:
            context["zipped_6k_results"] = sorted(zip(sixK_results[0], sixK_results[1], sixK_results[2], sixK_results[3], sixK_results[4]), key=lambda x: x[2], reverse=True)

        if eightK_results != [[], [], [], [], []]:
            context["zipped_8k_results"] = sorted(zip(eightK_results[0], eightK_results[1], eightK_results[2], eightK_results[3], eightK_results[4]), key=lambda x: x[2], reverse=True)


        return(context)




class MeetView(generic.ListView):
    template_name = 'myapp/meet.html'


    def get_queryset(self):
        return None



    def get_context_data(self, *args, **kwargs):
        context = super(generic.ListView, self).get_context_data(*args, **kwargs)

        meetData = str(self.kwargs['meetName']).replace(';', '').replace('  ', ' ').split("_")
        context["meet_name"] = meetData[0]
        context["meet_year"] = meetData[1]


        mens_results = RaceTime.objects.all().filter(gender="Male", meet=meetData[0], date__year=meetData[1]).order_by("place")
        womens_results = RaceTime.objects.all().filter(gender="Female", meet=meetData[0], date__year=meetData[1]).order_by("place")

        places = []
        scores = []
        teams = []
        names = []
        bibs = []
        times = []
        sessionOrders = []

        context["mens_event"] = mens_results[0].event


        sessions = [""]
        numberOfRaces = 0

        for i in range(len(mens_results)):
            if (len(mens_results[i].time) <= 8 and mens_results[i].firstName + " " + mens_results[i].lastName  not in names):
                places.append(mens_results[i].place)
                if mens_results[i].score == "None":
                    scores.append("N/A")
                else:
                    scores.append(mens_results[i].score)
                teams.append(mens_results[i].team)
                names.append(mens_results[i].firstName + " " + mens_results[i].lastName)
                bibs.append(mens_results[i].bib)
                times.append(mens_results[i].time)
                sessionOrders.append(mens_results[i].sessionOrder)
                if(mens_results[i].sessionOrder > numberOfRaces):
                    numberOfRaces = mens_results[i].sessionOrder
                    sessions.append("(" + mens_results[i].session + ")")









        # outer lists all race
        # inner lists hold places, scores, teams, names, bibs, times
        allMensResults = []
        # allMensResults.append([[], [], [], [], [], []])
        numberOfRaces += 1
        for i in range(numberOfRaces):
            allMensResults.append([[], [], [], [], [], []])


        # len(mensResults) == 904, but length of all other fields == 903 ?
        # placesLength = len(places)
        # scoresLength = len(scores)
        # teamsLength = len(teams)
        # bibsLength = len(bibs)
        # timesLength = len(times)
        # mens_results_length = len(mens_results)
        # lastResult = str(mens_results[903])

        for i in range(len(places)):

            allMensResults[sessionOrders[i]][0].append(places[i])
            allMensResults[sessionOrders[i]][1].append(scores[i])
            allMensResults[sessionOrders[i]][2].append(teams[i])
            allMensResults[sessionOrders[i]][3].append(names[i])
            allMensResults[sessionOrders[i]][4].append(bibs[i])
            allMensResults[sessionOrders[i]][5].append(times[i])



        for i in range(len(allMensResults)):
            allMensResults[i] = zip(allMensResults[i][0], allMensResults[i][1],allMensResults[i][2],allMensResults[i][3],allMensResults[i][4],allMensResults[i][5],)

        context["zipped_mens_results"] = zip(sessions, allMensResults)



        places = []
        scores = []
        teams = []
        names = []
        bibs = []
        times = []
        sessionOrders = []

        context["womens_event"] = womens_results[0].event

        sessions = [""]
        numberOfRaces = 0

        for i in range(len(womens_results)):
            if (len(womens_results[i].time) <= 8 and womens_results[i].firstName + " " + womens_results[i].lastName  not in names):
                places.append(womens_results[i].place)
                if womens_results[i].score == "None":
                    scores.append("N/A")
                else:
                    scores.append(womens_results[i].score)
                teams.append(womens_results[i].team)
                names.append(womens_results[i].firstName + " " + womens_results[i].lastName)
                bibs.append(womens_results[i].bib)
                times.append(womens_results[i].time)
                sessionOrders.append(womens_results[i].sessionOrder)
                if(womens_results[i].sessionOrder > numberOfRaces):
                    numberOfRaces = womens_results[i].sessionOrder
                    sessions.append("(" + womens_results[i].session + ")")


        # outer lists all race
        # inner lists hold places, scores, teams, names, bibs, times
        allWomensResults = []
        # allWomensResults.append([[], [], [], [], [], []])
        numberOfRaces += 1
        for i in range(numberOfRaces):
            allWomensResults.append([[], [], [], [], [], []])


        # len(womensResults) == 904, but length of all other fields == 903 ?
        # placesLength = len(places)
        # scoresLength = len(scores)
        # teamsLength = len(teams)
        # bibsLength = len(bibs)
        # timesLength = len(times)
        # womens_results_length = len(womens_results)
        # lastResult = str(womens_results[903])

        for i in range(len(places)):

            allWomensResults[sessionOrders[i]][0].append(places[i])
            allWomensResults[sessionOrders[i]][1].append(scores[i])
            allWomensResults[sessionOrders[i]][2].append(teams[i])
            allWomensResults[sessionOrders[i]][3].append(names[i])
            allWomensResults[sessionOrders[i]][4].append(bibs[i])
            allWomensResults[sessionOrders[i]][5].append(times[i])



        for i in range(len(allWomensResults)):
            allWomensResults[i] = zip(allWomensResults[i][0], allWomensResults[i][1],allWomensResults[i][2],allWomensResults[i][3],allWomensResults[i][4],allWomensResults[i][5],)



        context["zipped_womens_results"] = zip(sessions, allWomensResults)




        return context



# 'Multiple search boxes':  https://stackoverflow.com/questions/8735452/django-storing-queryset-in-request-session-still-queries-the-db-why



class TeamView(generic.ListView):
    template_name = 'myapp/Team.html'


    def get_queryset(self):
        return None



    def get_context_data(self, *args, **kwargs):
        context = super(generic.ListView, self).get_context_data(*args, **kwargs)

        teamData = str(self.kwargs['teamName']).replace(';', '').replace('  ', ' ').strip()
        context["team_name"] = teamData


        mens_results = RaceTime.objects.all().filter(gender="Male", team=str(teamData)).order_by("firstName")
        womens_results = RaceTime.objects.all().filter(gender="Female", team=teamData).order_by("firstName")



        names = []

        for result in mens_results:
            n = result.firstName + " " + result.lastName
            if n not in names:
                names.append(n)

        context["mens_results"] = names



        names = []

        for result in womens_results:
            n = result.firstName + " " + result.lastName
            if n not in names:
                names.append(n)

        context["womens_results"] = names


        return context




class AllMeetsView(generic.ListView):
    template_name = 'myapp/allMeets.html'
    context_object_name = 'allMeets_list'

    # Not currently used
    def get_queryset(self):

        empty = []
        return (empty)


    def get_context_data(self, *args, **kwargs):
        context = super(generic.ListView, self).get_context_data(*args, **kwargs)

        results = RaceTime.objects.all().order_by("date")


        meets = {}


        for result in results:
            meetName = result.meet + " (" + str(result.date.year) + ")"
            if(meetName not in meets):
                meets.update({meetName : {"date" : result.date, "events" : [result.event], "participants" : 1}})

            elif(result.event not in meets[meetName]["events"]):
                meets[meetName]["events"].append(result.event)
                meets[meetName]["participants"] += 1

            else:
                meets[meetName]["participants"] += 1





        # times(0), meets(1), dates(2), places(3), sessions(4)

        all_meets = [[], [], [], []]

        for m in meets.keys():
            all_meets[0].append(m.replace(" (2016)", "").replace(" (2015)", ""))
            all_meets[1].append(meets[m]["date"])
            all_meets[2].append(",".join(meets[m]["events"]))
            all_meets[3].append(meets[m]["participants"])






        # context["time"] = times
        # context["meet"] = meets
        # context["date"] = dates
        # context["places"] = places
        # context["rounds"] = rounds


        # times(0), meets(1), dates(2), places(3), sessions(4)



        context["zipped_meets"] = sorted(zip(all_meets[0], all_meets[1], all_meets[2], all_meets[3]), key=lambda x: x[1], reverse=True)


        return(context)