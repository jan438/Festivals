from reportlab.lib.pagesizes import A3, A4
from reportlab.pdfgen import canvas
import os

def create_pdf_template(filename, pagesize, title="Festivals"):
    """
    Creates a blank PDF template with a title.
    
    :param filename: Output PDF file name
    :param pagesize: Tuple (width, height) in points
    :param title: Title text to display on the page
    """
    try:
        c = canvas.Canvas(filename, pagesize=pagesize)
        width, height = pagesize

        # Draw title at the top center
        c.setFont("Helvetica-Bold", 24)
        c.drawCentredString(width / 2, height - 50, title)

        # Optional: Draw border
        c.setLineWidth(1)
        c.rect(20, 20, width - 40, height - 40)

        c.showPage()
        c.save()
        print(f"✅ PDF template '{filename}' created successfully.")
    except Exception as e:
        print(f"❌ Error creating PDF: {e}")

if __name__ == "__main__":
    os.makedirs("templates", exist_ok=True)

    # Create A4 template
    create_pdf_template("PDF/template_A4.pdf", A4, title="A4 Template")

    # Create A3 template
    create_pdf_template("PDF/template_A3.pdf", A3, title="A3 Template")
