import os
import sys
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import Color, red, blue, yellow, green, white, HexColor
from reportlab.lib.units import mm, cm

def drawRoundedRect(c, x, y, w, h, a, d, color1, color2, color3):    
    c.saveState()
    p = c.beginPath()
    p.moveTo(x, y + 0.5 * a)
    p.arcTo(x, y, x + a, y + a, startAng = 180, extent = 90)                # arc left below
    p.lineTo(x + w, y)                                                      # horizontal line
    p.arcTo(x + w, y, x + w + a, y + a, startAng = 270, extent = 90)        # arc right below
    p.lineTo(x + w + a, y + h)                                              # vertcal line
    p.arcTo(x + w, y + h, x + w + a, y + h + a, startAng = 0, extent = 90)  # arc right above
    p.lineTo(x + 0.5 * a, y + h + a)                                        # horizontal line
    p.arcTo(x, y + h, x + a, y + h + a, startAng = 90, extent = 90)         # arc left above
    p.lineTo(x, y + 0.5 * a)                                                # vertcal line
    c.drawPath(p, stroke = 0, fill = 1)
    c.clipPath(p, stroke=0)
    if d == 'd':
         c.linearGradient(x, y, x + w + a, y + h + a, (color1, color2, color3), (0, 0.5, 1))
    if d == 'h':
         c.linearGradient(x, y, x + w + a, y, (color1, color2, color3), (0, 0.5, 1))
    if d == 'v':
         c.linearGradient(x, y, x, y + h + a, (color1, color2, color3), (0, 0.5, 1))
    c.restoreState()

if sys.platform[0] == 'l':
    path = '/home/jan/git/Festivals'
if sys.platform[0] == 'w':
    path = "C:/Users/janbo/OneDrive/Documents/GitHub/Festivals"
os.chdir(path)
c = Canvas("PDF/Exercise.pdf", pagesize=letter)
drawRoundedRect(c, 11*cm,  12*cm, 50, 50, 20, 'd', "#da23ff", "#99ff99", "#9869ff")
red50transparent = Color( 100, 0, 0, alpha=0.5)
c.setFillColor(red50transparent)
c.rect(300,75,100,100, fill=True, stroke=False)
c.save()  

key = input("Wait")
