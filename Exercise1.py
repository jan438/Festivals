# Source - https://stackoverflow.com/q/73500497
# Posted by user15565396, modified by community. See post 'Timeline' for change history
# Retrieved 2026-05-30, License - CC BY-SA 4.0

import numpy as np
import matplotlib.pyplot as plt
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, landscape, A4
from reportlab.lib.utils import ImageReader

fig = plt.figure()
#fig.patch.set_facecolor('#0c1c33')
#fig.patch.set_alpha(1)
data = [10,30,25,15,10]
plt.pie(data, labels = ['A', 'B', 'C', 'D', 'E'])
circle = plt.Circle( (0,0), 0.7, color='#0c1c33')
p = plt.gcf()
p.gca().add_artist(circle)
plt.savefig('PDF/test_donut.png')
plt.show()

my_canvas = canvas.Canvas("PDF/Test_Rapport.pdf",pagesize=(landscape(A4)),bottomup=0)
my_canvas.drawImage(ImageReader('PDF/test_donut.png'), 300, 150, width=200, height=150)
my_canvas.save()

key = input("Wait")
