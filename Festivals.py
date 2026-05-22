from reportlab.lib.pagesizes import A3, A4
from reportlab.pdfgen import canvas
import os

def create_pdf_template(filename, pagesize, title="Festivals"):
    try:
        c = canvas.Canvas(filename, pagesize=pagesize)
        width, height = pagesize
        c.setFont("Helvetica-Bold", 24)
        c.drawCentredString(width / 2, height - 50, title)
        c.setLineWidth(1)
        c.rect(20, 20, width - 40, height - 40)
        c.showPage()
        c.save()
        print(f"✅ PDF template '{filename}' created successfully.")
    except Exception as e:
        print(f"❌ Error creating PDF: {e}")


create_pdf_template("PDF/Festivals_A4.pdf", A4, title="A4 Template")
create_pdf_template("PDF/Festivals_A3.pdf", A3, title="A3 Template")

key = input("Wait")
