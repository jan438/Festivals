from reportlab.lib.pagesizes import A3, A4
from reportlab.pdfgen import canvas
import os
import csv
import sys
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFontFamily

festivalfont = "LiberationSerif"
templatedata = []

def create_Fesival_pdf(filename, ps, pagesize, title="Festivals"):
    try:
        c = canvas.Canvas(filename, pagesize=pagesize)
        width, height = pagesize
        titlefontsize_value = variable_dict["titlefontsize" + ps]
        titley_value = variable_dict["titley" + ps]
        namewidth = pdfmetrics.stringWidth(title, festivalfont, titlefontsize_value)
        c.setFont(festivalfont, titlefontsize_value)
        c.drawCentredString(width / 2, height - titley_value, title)
        c.setLineWidth(1)
        c.rect(20, 20, width - 40, height - 40)
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

file_to_open = "Data/template.csv"
with open(file_to_open, 'r') as file:
    csvreader = csv.reader(file, delimiter = ';')
    count = 0
    for row in csvreader:
        templatedata.append(row)
        count += 1
print(count)

variable_dict = {}

variable_dict['titlefontsizeA3'] = 42
variable_dict['titlefontsizeA4'] = 21
variable_dict['titleyA3'] = 50
variable_dict['titleyA4'] = 40

create_Fesival_pdf("PDF/Festivals_A4.pdf", "A4", A4, title="A4 Festivals")
create_Fesival_pdf("PDF/Festivals_A3.pdf", "A3", A3, title="A3 Festivals")

key = input("Wait")
