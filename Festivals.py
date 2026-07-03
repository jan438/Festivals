from reportlab.lib.pagesizes import A3, A4
from reportlab.pdfgen import canvas
import os
import csv
import sys
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFontFamily
from svglib.svglib import svg2rlg, load_svg_file, SvgRenderer
from reportlab.graphics import renderPDF
from reportlab.lib.colors import yellow, green, red, black, HexColor
from reportlab.lib.colors import tan, black, green
from reportlab.lib.units import inch, cm, mm
from math import pi, cos, sin, radians, sqrt

festivalfont = "LiberationSerif"
festivaldata = []
templatedata = []
festivalevents = []
maxfestivals = 10
maxfestivalspage = 25

class FestivalEvent:
    def __init__(self, summary, startday, endday, location, description, month):
        self.summary = summary
        self.location = location
        self.description = description
        self.startday = startday
        self.endday = endday
        self.month = month
        
def weekDay(year, month, day):
    offset = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    afterFeb = 1
    if month > 2: afterFeb = 0
    aux = year - 1700 - afterFeb
    dayOfWeek  = 5
    dayOfWeek += (aux + afterFeb) * 365                  
    dayOfWeek += aux / 4 - aux / 100 + (aux + 100) / 400     
    dayOfWeek += offset[month - 1] + (day - 1)               
    dayOfWeek %= 7
    return round(dayOfWeek)
        
def scaleSVG(svgfile, scaling_factor):
    svg_root = load_svg_file(svgfile)
    svgRenderer = SvgRenderer(svgfile)
    drawing = svgRenderer.render(svg_root)
    scaling_x = scaling_factor
    scaling_y = scaling_factor
    drawing.width = drawing.minWidth() * scaling_x
    drawing.height = drawing.height * scaling_y
    drawing.scale(scaling_x, scaling_y)
    return drawing
    
def drawallroundRect(c, x, y, w, h, a, color):    
    c.setFillColor(HexColor(color))
    p = c.beginPath()
    p.moveTo(x, y + 0.5 * a)
    p.arcTo(x, y, x + a, y + a, startAng = 180, extent = 90)
    p.lineTo(x + w, y)
    p.arcTo(x + w, y, x + w + a, y + a, startAng = 270, extent = 90)
    p.lineTo(x + w + a, y + h)
    p.arcTo(x + w, y + h, x + w + a, y + h + a, startAng = 0, extent = 90)
    p.lineTo(x + 0.5 * a, y + h + a)
    p.arcTo(x, y + h, x + a, y + h + a, startAng = 90, extent = 90)
    p.lineTo(x, y + 0.5 * a)
    c.drawPath(p, stroke = 0, fill = 1)
    
def drawrightroundRect(c, x, y, w, h, a, color):    
    c.setFillColor(HexColor(color))
    p = c.beginPath()
    p.moveTo(x + 0.5 * a, y)
    p.lineTo(x + 0.5 * a + w, y)
    p.arcTo(x + w, y, x + w + a, y + a, startAng = 270, extent = 90)
    p.lineTo(x + w + a, y + h)
    p.arcTo(x + w, y + h, x + w + a, y + h + a, startAng = 0, extent = 90)
    p.lineTo(x + 0.5 * a, y + h + a)
    p.lineTo(x + 0.5 * a, y + 0.5 * a)
    c.drawPath(p, stroke = 0, fill = 1)
    
def drawleftroundRect(c, x, y, w, h, a, color):    
    c.setFillColor(HexColor(color))
    p = c.beginPath()
    p.moveTo(x, y + 0.5 * a)
    p.arcTo(x, y, x + a, y + a, startAng = 180, extent = 90)
    p.lineTo(x + w + 0.5 * a, y)
    p.lineTo(x + w + 0.5 * a, y + h + a)
    p.lineTo(x + 0.5 * a, y + h + a)
    p.arcTo(x, y + h, x + a, y + h + a, startAng = 90, extent = 90)
    p.lineTo(x, y + 0.5 * a)
    c.drawPath(p, stroke = 0, fill = 1)
    
def drawtoproundRect(c, x, y, w, h, a, color):    
    c.setFillColor(HexColor(color))
    p = c.beginPath()
    p.moveTo(x, y + 0.5 * a)
    p.lineTo(x + w + a, y + 0.5 * a)
    p.lineTo(x + w + a, y + h)
    p.arcTo(x + w, y + h, x + w + a, y + h + a, startAng = 0, extent = 90)
    p.lineTo(x + 0.5 * a, y + h + a)
    p.arcTo(x, y + h, x + a, y + h + a, startAng = 90, extent = 90)
    p.lineTo(x, y + 0.5 * a)
    c.drawPath(p, stroke = 0, fill = 1)
    
def drawbottomroundRect(c, x, y, w, h, a, color):    
    c.setFillColor(HexColor(color))
    p = c.beginPath()
    p.moveTo(x, y + 0.5 * a)
    p.arcTo(x, y, x + a, y + a, startAng = 180, extent = 90)
    p.lineTo(x + w, y)
    p.arcTo(x + w, y, x + w + a, y + a, startAng = 270, extent = 90)
    p.lineTo(x + w + a, y + h + 0.5 * a)
    p.lineTo(x, y + h + 0.5 * a)
    p.lineTo(x, y + 0.5 * a)
    c.drawPath(p, stroke = 0, fill = 1)
  
def create_Fesival_pdf(filename, ps, pagesize, title="Festivals"):
    row = 25
    col = 0
    position = 500
    try:
        c = canvas.Canvas(filename, pagesize=pagesize)
        c.setTitle(title)
        width, height = pagesize
        c.setFillColor(HexColor('#FECDE5'))
        c.rect(0, 0, width, height, fill=1)
        #cadre(c, pagesize)
        c.setTitle("Festivals 2026")
        count = 0
        for i in range(len(festivalevents)):
            c.setFillColor(HexColor('#000000'))
            c.setFont(festivalfont, 12)
            c.drawString(leftmargin + col * colwidth + 50, bottommargin + row * rowheight, festivalevents[i].summary)
            c.drawString(leftmargin + col * colwidth + 150, bottommargin + row * rowheight, festivalevents[i].location)
            c.drawString(leftmargin + col * colwidth + 250, bottommargin + row * rowheight, festivalevents[i].description)
            print(i, festivalevents[i].startday, festivalevents[i].endday)
            row -= 1
            count += 1
            position -= 1
            if count == maxfestivalspage:
                c.showPage()
                position = 500
                count = 0
                row = 25
                col = 0
                c.setFillColor(HexColor('#FECDE5'))
                c.rect(0, 0, width, height, fill=1)
        c.showPage()
        c.save()
        print(f"✅ PDF Festivals '{filename}' created successfully.")
    except Exception as e:
        print(f"❌ Error creating PDF: {e}")
        
if sys.platform[0] == 'l':
    path = '/home/jan/git/Festivals'
if sys.platform[0] == 'w':
    path = "C:/Users/janbo/OneDrive/Documents/GitHub/Festivals"
os.chdir(path)
pdfmetrics.registerFont(TTFont('LiberationSerif', 'LiberationSerif-Regular.ttf'))
pdfmetrics.registerFont(TTFont('LiberationSerifBold', 'LiberationSerif-Bold.ttf'))
pdfmetrics.registerFont(TTFont('LiberationSerifItalic', 'LiberationSerif-Italic.ttf'))
pdfmetrics.registerFont(TTFont('LiberationSerifBoldItalic', 'LiberationSerif-BoldItalic.ttf'))
file_to_open = "Data/FestivalsInternational.csv"
with open(file_to_open, 'r') as file:
    csvreader = csv.reader(file, delimiter = ';')
    count = 0
    for row in csvreader:
        festivaldata.append(row)
        count += 1
print(count)
file_to_open = "Data/template.csv"
with open(file_to_open, 'r') as file:
    csvreader = csv.reader(file, delimiter = ';')
    count = 0
    for row in csvreader:
        templatedata.append(row)
        count += 1
print(count)
festivalcal = "Calendar/Festivals2026.ics"
in_file = open(os.path.join(path, festivalcal), 'r')
count = 0
lastpos = 0
found = 0
alleventslines = []
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
    locationeventpos = alleventslines[i].find("LOCATION")
    descriptioneventpos = alleventslines[i].find("DESCRIPTION")
    dtstarteventpos = alleventslines[i].find("DTSTART")
    dtendeventpos = alleventslines[i].find("DTEND")
    endeventpos = alleventslines[i].find("END:VEVENT")
    if neweventpos == 0:
        summary = ""
        day = 0
        location = ""
        description = ""
        starttime = 0
        endtime = 0
        month = 0
    if dtstarteventpos == 0:
        eventdtstartstr = alleventslines[i][8:]
        datevaluepos = alleventslines[i].find("VALUE=DATE:")
        if datevaluepos == 8:
            eventdtstartstr = alleventslines[i][19:]
        year = int(eventdtstartstr[:4])
        month = int(eventdtstartstr[4:6])
        startday = int(eventdtstartstr[6:8])
        weekday = weekDay(year, month, startday)
    if dtendeventpos == 0:
        eventdtendstr = alleventslines[i][6:]
        year = int(eventdtendstr[:4])
        month = int(eventdtendstr[4:6])
        endday = int(eventdtendstr[6:8])
        weekday = weekDay(year, month, endday)
    if summaryeventpos == 0:
        summary = alleventslines[i][8:]
    if locationeventpos == 0:
        location = alleventslines[i][9:]
    if descriptioneventpos == 0:
        description = alleventslines[i][12:]
    if endeventpos == 0:
        festivalevents.append(FestivalEvent(summary, startday, endday, location, description, month))
print("Count festival events", len(festivalevents))
colwidth = 200
rowheight = 20
leftmargin = 10
bottommargin = 100
variable_dict = {}
for i in range(len(templatedata)):
    variable_dict[templatedata[i][0]] = float(templatedata[i][1])
create_Fesival_pdf("PDF/Festivals_A4.pdf", "A4", A4, title="A4 Festivals")
create_Fesival_pdf("PDF/Festivals_A3.pdf", "A3", A3, title="A3 Festivals")

key = input("Wait")
