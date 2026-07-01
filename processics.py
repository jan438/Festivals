import os
from datetime import datetime, date, timedelta
import pytz
import os
import sys
import csv
import math
import unicodedata
from ics import Calendar, Event
from datetime import datetime, timezone, timedelta

alleventslines = []
festivalevents = []

class FestivalEvent:
    def __init__(self, summary, startday, endday, description, location, month):
        self.summary = summary
        self.startday = startday
        self.endday = endday
        self.description = description
        self.location = location
        self.month = month
        
def addFestivalEvent(summary, startday, endday, description, location, month):
    festivalevents.append(FestivalEvent(summary, startday, endday, description, location, month))

def converttimetztolocalclock(timetz):
    utc_string = timetz
    utc_format = "%Y%m%dT%H%M"
    local_tz = pytz.timezone('Europe/Amsterdam')
    utc_dt = datetime.strptime(utc_string, utc_format)
    local_dt = utc_dt
    hour = local_dt.hour
    minute = local_dt.minute
    return [hour, minute]
    
if sys.platform[0] == 'l':
    path = '/home/jan/git/Festivals'
if sys.platform[0] == 'w':
    path = "C:/Users/janbo/OneDrive/Documents/GitHub/Festivals"
os.chdir(path)
eventcal = "Calendar/Festivals2026.ics"
in_file = open(os.path.join(path, eventcal), 'r')
count = 0
lastpos = 0
for line in in_file:
    newlinepos = line.find("\t\n")
    lastsubstring = line[lastpos:newlinepos]
    alleventslines.append(lastsubstring)
    count += 1
in_file.close()
print("Count eventslines", len(alleventslines))
for i in range(len(alleventslines)):
    neweventpos = alleventslines[i].find("BEGIN:VEVENT")
    summaryeventpos = alleventslines[i].find("SUMMARY")
    descriptioneventpos = alleventslines[i].find("DESCRIPTION")
    locationeventpos = alleventslines[i].find("LOCATION")
    dtstarteventpos = alleventslines[i].find("DTSTART")
    dtendeventpos = alleventslines[i].find("DTEND")
    endeventpos = alleventslines[i].find("END:VEVENT")
    if neweventpos == 0:
        summary = ""
        startday = 0
        endday = 0
        description = ""
        location = ""
        month = 0
    if dtstarteventpos == 0:
        eventdtstartstr = alleventslines[i][8:]
        datevaluepos = alleventslines[i].find("VALUE=DATE:")
        if datevaluepos == 8:
            eventdtstartstr = alleventslines[i][19:]
        print("startime", eventdtstartstr)
        startday = int(eventdtstartstr[6:8])
    if dtendeventpos == 0:
        eventdtendstr = alleventslines[i][17:]
        datevaluepos = alleventslines[i].find("VALUE=DATE:")
        if datevaluepos == 8:
            eventdtendstr = alleventslines[i][17:]
        year = int(eventdtendstr[:4])
        month = int(eventdtendstr[4:6])
        endday = int(eventdtendstr[6:8])
        print("endtime",eventdtendstr, year, month, endday)
    if summaryeventpos == 0:
        summary = alleventslines[i][8:]
    if descriptioneventpos == 0:
        description = alleventslines[i][12:]
    if locationeventpos == 0:
        location = alleventslines[i][9:]
    if endeventpos == 0:
        festivalevents.append(FestivalEvent(summary, startday, endday, description, location, month))
print("Count festival events", len(festivalevents))

c = Calendar()
for i in range(len(festivalevents)):
    e = Event()
    e.name = festivalevents[i].summary
    e.description = festivalevents[i].description
    e.location = festivalevents[i].location
    c.events.add(e)
    
summary = "summary"
start = "start"
end= "end"
des = "des"
loc = "loc"
month = "month"
addFestivalEvent("summary", "start", "end", "des", "loc", "month")
    
#e = Event()
#e.name = festivalevents[i].summary
#e.description = festivalevents[i].description
#e.location = festivalevents[i].location
#c.events.add(e)

with open("Calendar/Festivals2026.ics", "w") as f:
    f.writelines(c)
    f.close()

key = input("Wait")
