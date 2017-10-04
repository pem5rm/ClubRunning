#Data Format:  {Name : [Event, Meet, Date, Team, Place, Time, session]}
#CSV Format: place, first name, last name, team, time, session, event, meet, date




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
parseEventData2("100m", "Nats", "31")