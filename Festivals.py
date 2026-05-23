from reportlab.lib.pagesizes import A3, A4
from reportlab.pdfgen import canvas
import os
import sys
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFontFamily

festivalfont = "LiberationSerif"
titlefontsizeA3 = 30
titlefontsizeA4 = 24

def create_Fesival_pdf(filename, pagesize, title="Festivals"):
    variable_dict = {}
    titlefontsizeA3_name = 'titlefontsizeA3'
    titlefontsizeA3_value = 42
    variable_dict[titlefontsizeA3_name] = titlefontsizeA3_value
    retrieved_value = variable_dict[titlefontsizeA3_name]
    print(f'{titlefontsizeA3_name}: {retrieved_value}')
    try:
        c = canvas.Canvas(filename, pagesize=pagesize)
        width, height = pagesize
        print(f'Pagesize "{pagesize}"')
        if pagesize == A3:
            namewidth = pdfmetrics.stringWidth(title, festivalfont, titlefontsizeA3)
            c.setFont(festivalfont, titlefontsizeA3)
        if pagesize == A4:
            namewidth = pdfmetrics.stringWidth(title, festivalfont, titlefontsizeA4)
            c.setFont(festivalfont, titlefontsizeA4)
        c.drawCentredString(width / 2, height - 50, title)
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

create_Fesival_pdf("PDF/Festivals_A4.pdf", A4, title="A4 Festivals")
create_Fesival_pdf("PDF/Festivals_A3.pdf", A3, title="A3 Festivals")

key = input("Wait")
