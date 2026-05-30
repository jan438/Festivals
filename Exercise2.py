# Source - https://stackoverflow.com/a/73527452
# Posted by Conor, modified by community. See post 'Timeline' for change history
# Retrieved 2026-05-30, License - CC BY-SA 4.0

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, landscape, A4
from reportlab.lib.utils import ImageReader

my_canvas = canvas.Canvas("PDF/Test_Rapport2.pdf",pagesize=(landscape(A4)),bottomup=0)

my_canvas.saveState()
my_canvas.scale(1,-1)
x_val = 300
y_val = -150
my_canvas.drawImage(ImageReader('PDF/test_donut.png'), x_val, y_val, width=200, height=150)
my_canvas.restoreState()

my_canvas.save()

key = input("Wait")
