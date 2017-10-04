# CURRENT PROGRESS:
# Finished up to (and including): Harvard XC Invite 2015


# TO DO: missing results:
# Spartan Grand Classic 2016
# St. John's University Fall XC Festival 2016
# SJUTC Pumpkin Challenge 2016
# UML Club Track Fall Invitational 2016
# NIRCA XC Nationals Open 5k 2016
# Penn Sprint Classic 2016


#Data Format:  {Name : [Event, Meet, Date, Team, Place, Time, Round]}
#CSV Format: place, first name, last name, team, time, round, event, meet, date

#New Format: place, firstName, lastName, team, time, session, even, meet, date, score, bib, location, host, gender

def parseOldEventData(event, meet, date, location, host, gender, bib="N/A", session="N/A"):

    file = open("rawData.txt", "r")
    file2 = open("nircaData.csv", "a")

    for line in file:
        line = line.replace("(> 7)", "").replace("(", "").replace(")", "")
        line = line.strip().split()

        #if there is a score
        if line[1].isdigit():
            score = line[1]
            line.remove(line[1])
        elif line[1] == "-":
            line.remove(line[1])
            score = "None"
        else:
            score = "None"

        if line[-2].isdigit():
            bib = line[-2]
            line.remove(line[-2])
        else:
            bib = "N/A"

        place = line[0]
        del line[0]
        time = line[-1]
        del line[-1]
        first = line[-1]
        del line[-1]
        last = line[-1]
        del line[-1]
        team = " ".join(line)

        if gender == "0":
            gender = "Male"
        elif gender == "1":
            gender = "Female"


        file2.write(place.strip() + ";" + first.strip() + ";" + last.strip() + ";" + team.strip() + ";" + time.strip() + ";" + session.strip() + ";" + event.strip() + ";" + meet.strip() + ";" + date.strip() + ";" + score.strip() + ";" + bib.strip() + ";" + location.strip() + ";" + host.strip() + ";" + gender.strip() + "\n")
    file.close()
    file2.close()


def parseEventData(event, meet, date, location, host, gender, bib="N/A", session="N/A"):

    file = open("rawData.txt", "r")
    file2 = open("nircaData.csv", "a")

    for line in file:
        line = line.replace("(> 7)", "").replace("(", "").replace(")", "")
        line = line.strip().split()

        #if there is a score
        if line[1].isdigit():
            score = line[1]
            line.remove(line[1])
        elif line[1] == "-":
            line.remove(line[1])
            score = "None"
        else:
            score = "None"

        if line[-2].isdigit():
            bib = line[-2]
            line.remove(line[-2])
        else:
            bib = "N/A"

        place = line[0]
        del line[0]
        time = line[-1]
        del line[-1]
        first = line[-1]
        del line[-1]
        last = line[-1]
        del line[-1]
        team = " ".join(line)

        if gender == "0":
            gender = "Male"
        elif gender == "1":
            gender = "Female"


        file2.write(place.strip() + ";" + first.strip() + ";" + last.strip() + ";" + team.strip() + ";" + time.strip() + ";" + session.strip() + ";" + event.strip() + ";" + meet.strip() + ";" + date.strip() + ";" + score.strip() + ";" + bib.strip() + ";" + location.strip() + ";" + host.strip() + ";" + gender.strip() + "\n")
    file.close()
    file2.close()

# def parseEventData(event, meet, date, location, host, gender, bib="N/A", session="N/A"):


parseEventData("6K", "Pacific Regional", "2016-10-29 00:00:00", "Crystal Springs Cross Country Course", "NIRCA and NU Club Running", "1")








def parseEventData2(event, meet, date):
    file = open("rawData.txt", "r")
    file2 = open("nircaData.csv", "a")

    for line in file:
        line = line.strip().split()
        if (len(line) == 5 or len(line) == 6):
            # print(line)
            file2.write(",".join(line[0:5]) + ",Prelims," + event + "," + meet + "," + date + "\n")
            if(len(line) == 6):
                # del(line[5])
                # file2.write(",".join(line) + ",Prelims," + event + "," + meet + "," + date + "\n")
                #
                # # print(line)
                # del(line[4])
                # print(line)
                file2.write(",".join(line[0:4]) + "," + line[5] + ",Finals," + event + "," + meet + "," + date + "\n")

        else:
            print("Error Wrong Line Length:  " + ",".join(line))
    file.close()
    file2.close()
# parseEventData2("100m", "Nats", "2017-07-13 00:00:00")



#parseEventData Old Version with Commas
def parseEventDataOLD(event, meet, date, location, host, gender, bib="N/A", session="N/A"):

    file = open("rawData.txt", "r")
    file2 = open("nircaData.csv", "a")

    for line in file:
        line = line.strip().split()

        #if there is a score
        if line[1].isdigit():
            score = line[1]
            line.remove(line[1])
        elif line[1] == "-":
            line.remove(line[1])
            score = "None"
        else:
            score = "None"

        if line[-2].isdigit():
            bib = line[-2]
            line.remove(line[-2])
        else:
            bib = "N/A"

        place = line[0]
        del line[0]
        time = line[-1]
        del line[-1]
        first = line[-1]
        del line[-1]
        last = line[-1]
        del line[-1]
        team = " ".join(line)

        if gender == "0":
            gender = "Male"
        elif gender == "1":
            gender = "Female"

        file2.write(place.strip() + "," + first.strip() + "," + last.strip() + "," + team.strip() + "," + time.strip() + "," + session.strip() + "," + event.strip() + "," + meet.strip() + "," + date.strip() + "," + score.strip() + "," + bib.strip() + "," + location.strip() + "," + host.strip() + "," + gender.strip() + "\n")
    file.close()
    file2.close()

