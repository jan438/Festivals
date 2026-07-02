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
    
def addEvent(c, summary, startday, endday, description, location, month, year):
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
summary = "Rock Werchter"
start = 2
end= 5
des = "Rock Werchter viert in 2026 weer een nieuwe editie. Het 4-daagse festival vind plaats op donderdag 2 t/m zondag 5 Juli in Belgie."
loc = "Werchter"
month = 7
year = 2026
addEvent(c, "summary", start, end, "des", "loc", month, year)

with open("Calendar/Festivals.ics", "w") as f:
    f.writelines(c)
    f.close()
key = input("Wait")
