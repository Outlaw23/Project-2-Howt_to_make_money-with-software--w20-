import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors

def generate_invoice():
    if not os.path.exists('PDF_INVOICE'):
        os.makedirs('PDF_INVOICE')
    filename = 'PDF_INVOICE/factuur_template.pdf'

    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter

    c.setFont("Helvetica-Bold", 16)
    c.drawString(220, height - 40, "Factuur")

    c.setFont("Helvetica", 12)
    c.drawString(30, height - 80, "Paper Code")
    c.drawString(30, height - 100, "Puzzelpap")
    c.drawString(30, height - 120, "2367YU Antwerpen")
    c.drawString(30, height - 140, "+32 069876543")
    c.drawString(30, height - 160, "PaperCode@outlook.com")

    c.setFont("Helvetica", 12)
    c.drawString(300, height - 80, "Peters der West")
    c.drawString(300, height - 100, "Colaweg 43")
    c.drawString(300, height - 120, "5690RT Rotterdam")
    c.drawString(300, height - 140, "Tel: 098-7654321")

    c.setFont("Helvetica", 12)
    c.drawString(400, height - 80, "Factuurnummer: 546774")
    c.drawString(400, height - 100, "Datum: 23-04-2015")

    c.setStrokeColor(colors.black)
    c.setLineWidth(1)
    c.line(30, height - 180, width - 30, height - 180)

    c.setFont("Helvetica-Bold", 12)
    c.drawString(30, height - 200, "Omschrijving")
    c.drawString(300, height - 200, "Aantal")
    c.drawString(400, height - 200, "Prijs")

    c.line(30, height - 210, width - 30, height - 210)

    c.setFont("Helvetica", 12)
    for i in range(5):
        c.drawString(30, height - 230 - (i * 20), "Omschrijving product %d" % (i + 1))
        c.drawString(300, height - 230 - (i * 20), "X")
        c.drawString(400, height - 230 - (i * 20), "€ 0,00")

    c.setFont("Helvetica-Bold", 12)
    c.drawString(300, height - 330, "Totaal:")

    c.line(30, height - 340, width - 30, height - 340)

    c.save()

    print(f'Factuursjabloon gegenereerd: {filename}')

if __name__ == '__main__':
    generate_invoice()
