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
    def __init__(self, summary, startday, endday, description, location, month, year):
        self.summary = summary
        self.startday = startday
        self.endday = endday
        self.description = description
        self.location = location
        self.month = month
        self.year = year
        
def addFestivalEvent(summary, startday, endday, description, location, month, year):
    festivalevents.append(FestivalEvent(summary, startday, endday, description, location, month, year))

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
c = Calendar()
summary = "summary"
start = 12
end= 14
des = "des"
loc = "loc"
month = 12
year = 2026
addFestivalEvent("summary", start, end, "des", "loc", month, year)
e = Event()
e.name = summary
e.description = des
e.location = loc
e.begin = e.begin = datetime(
        year,
        month,
        day=start,
        hour=0,
        minute=0,
        second=0,
        tzinfo=None
    )
e.end = e.end = datetime(
        year,
        month,
        day=end,
        hour=0,
        minute=0,
        second=0,
        tzinfo=None
    )
c.events.add(e)
with open("Calendar/Festivals.ics", "w") as f:
    f.writelines(c)
    f.close()
key = input("Wait")
