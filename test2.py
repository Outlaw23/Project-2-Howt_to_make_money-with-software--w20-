from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import json

with open('factuur.json', 'r') as f:
    factuur_data = json.load(f)

pdf_file = "factuur.pdf"
c = canvas.Canvas(pdf_file, pagesize=letter)

c.setFont("Helvetica-Bold", 16)
c.drawString(220, 750, "Factuur")

c.setFont("Helvetica", 12)
c.drawString(30, 720, f'Klant: {factuur_data["klant"]["naam"]}')
c.drawString(30, 705, f'Adres: {factuur_data["klant"]["adres"]}')
c.drawString(30, 690, f'Postcode: {factuur_data["klant"]["postcode"]}')
c.drawString(30, 675, f'Stad: {factuur_data["klant"]["stad"]}')
c.drawString(30, 660, f'Factuurnummer: {factuur_data["order"]["ordernummer"]}')
c.drawString(30, 645, f'Datum: {factuur_data["order"]["orderdatum"]}')

c.setFont("Helvetica-Bold", 12)
c.drawString(30, 630, "Producten:")

c.setFont("Helvetica", 12)
y_position = 615
for product in factuur_data['producten']:
    c.drawString(30, y_position, f"{factuur_data['producten']['productnaam']} - €{int(factuur_data['producten']['prijs_per_stuk_excl_btw'])} x {int(factuur_data['producten']['aantal'])} = €{int(factuur_data['producten']['totaalKosten'])}")
    y_position -= 15

c.setFont("Helvetica-Bold", 12)
c.drawString(30, y_position - 20, f"Totaalbedrag: €{factuur_data['producten']['tota alKosten']}")

c.save()

print("Factuur PDF is gegenereerd: factuur.pdf")