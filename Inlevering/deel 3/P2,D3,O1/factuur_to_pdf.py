from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import json

with open('factuur.json', 'r') as f:
    factuur_data = json.load(f)

pdf_file = "factuur.pdf"
c = canvas.Canvas(pdf_file, pagesize=letter)
width, height = letter

c.setFont("Helvetica-Bold", 16)
c.drawString(220, height - 40, "Factuur")

c.setFont("Helvetica", 12)
c.drawString(30, height - 80, factuur_data["company"]["name"])
c.drawString(30, height - 100, factuur_data["company"]["address"])
c.drawString(30, height - 120, factuur_data["company"]["postcode"])
c.drawString(30, height - 140, factuur_data["company"]["phone"])
c.drawString(30, height - 160, factuur_data["company"]["email"])

c.setFont("Helvetica", 12)
c.drawString(300, height - 80, factuur_data["klant"]["naam"])
c.drawString(300, height - 100, factuur_data["klant"]["adres"])
c.drawString(300, height - 120, factuur_data["klant"]["postcode"])

c.setFont("Helvetica", 12)
c.drawString(400, height - 80, f"Factuurnummer: {factuur_data['order']['ordernummer']}")
c.drawString(400, height - 100, f"Datum: {factuur_data['order']['orderdatum']}")

c.setStrokeColor(colors.black)
c.setLineWidth(1)
c.line(30, height - 180, width - 30, height - 180)

c.setFont("Helvetica-Bold", 12)
c.drawString(30, height - 200, factuur_data["producten"]["productnaam"])
c.drawString(300, height - 200, str(factuur_data["producten"]["aantal"]))
c.drawString(400, height - 200, str(factuur_data["producten"]["prijs_per_stuk_excl_btw"]))

c.line(30, height - 210, width - 30, height - 210)

c.setFont("Helvetica", 12)
for i in range(factuur_data["producten"]["aantal"]):
    c.drawString(30, height - 230 - (i * 20), "Omschrijving product %d" % (i + 1))
    c.drawString(300, height - 230 - (i * 20), "X")
    c.drawString(400, height - 230 - (i * 20), "€ 0,00")

c.setFont("Helvetica-Bold", 12)
c.drawString(300, height - 330, "Totaal:")

c.line(30, height - 340, width - 30, height - 340)

c.drawImage("logo.png", 30, height - 60, width=50, height=50)



c.save()

print("Factuur PDF is gegenereerd: factuur.pdf")