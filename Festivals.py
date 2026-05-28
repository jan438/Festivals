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
from reportlab.lib.colors import HexColor
from reportlab.lib.colors import tan, black, green
from reportlab.lib.units import inch, cm, mm

festivalfont = "LiberationSerif"
templatedata = []

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
    
def cadre(c, pagesize):
    width = pagesize[0]
    height = pagesize[1]
    dx = width / 10
    for i in range(11):
        c.line(i * dx, 0, i * dx, height)
    for i in range(15):
        c.line(0, i * dx, width, i * dx)

def penciltip(c, x, y, debug=1):
    u = cm/10.0
    c.setLineWidth(4)
    if debug:
        c.scale(2.8,2.8) # make it big
        c.setLineWidth(1) # small lines
    c.setStrokeColor(black)
    c.setFillColor(tan)
    p = c.beginPath()
    p.moveTo(x+10*u,y)
    p.lineTo(x,y+5*u)
    p.lineTo(x+10*u,y+10*u)
    p.curveTo(x+11.5*u,y+10*u, x+11.5*u,y+7.5*u, x+10*u,y+7.5*u)
    p.curveTo(x+12*u,y+7.5*u, x+11*u,y+2.5*u, x+9.7*u,y+2.5*u)
    p.curveTo(x+10.5*u,y+2.5*u, x+11*u,y, x+10*u,y)
    c.drawPath(p, stroke=1, fill=1)
    c.setFillColor(black)
    p = c.beginPath()
    p.moveTo(x,y+5*u)
    p.lineTo(x+4*u,y+3*u)
    p.lineTo(x+5*u,y+4.5*u)
    p.lineTo(x+3*u,y+6.5*u)
    c.drawPath(p, stroke=1, fill=1)
    if debug:
        c.setStrokeColor(green) # put in a frame of reference
        c.grid([x,x+5*u,x+10*u,x+15*u], [y,y+5*u,y+10*u])
        
def create_Fesival_pdf(filename, ps, pagesize, title="Festivals"):
    try:
        c = canvas.Canvas(filename, pagesize=pagesize)
        width, height = pagesize
        c.setFillColor(HexColor('#FECDE5'))
        c.rect(0, 0, width, height, fill=1)
        c.setFillColor(HexColor('#000000'))
        cadre(c, pagesize)
        titlefontsize_value = variable_dict["titlefontsize" + ps]
        titley_value = variable_dict["titley" + ps]
        namewidth = pdfmetrics.stringWidth(title, festivalfont, titlefontsize_value)
        c.setFont(festivalfont, titlefontsize_value)
        c.drawCentredString(width / 2, height - titley_value, title)
        c.setLineWidth(1)
        c.rect(325, 444, 40, 40)
        scale_value = variable_dict["scaleinfobox" + ps]
        drawing = scaleSVG('SVG/infobox.svg', float(scale_value))
        renderPDF.draw(drawing, c, 150, 475)
        dy = width / 10
        drawallroundRect(c,  30,  dy, 1, 1, 50, "#80ff84")
        drawrightroundRect(c,  230,  dy, 1, 40, 50, "#80ff84")
        drawleftroundRect(c,  430,  dy, 1, 40, 50, "#80ff84")
        drawtoproundRect(c,  230,  3 * dy, 40, 40, 50, "#80ff84")
        penciltip(c, 10, 50, True)
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

for i in range(len(templatedata)):
    variable_dict[templatedata[i][0]] = float(templatedata[i][1])

create_Fesival_pdf("PDF/Festivals_A4.pdf", "A4", A4, title="A4 Festivals")
create_Fesival_pdf("PDF/Festivals_A3.pdf", "A3", A3, title="A3 Festivals")

key = input("Wait")
