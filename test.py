import json
import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors

# BTW percentage
BTW_PERCENTAGE = 21

# Afronden op 5 cent
def round_to_nearest_5_cent(value):
    return round(value * 20) / 20

# Functie om een order om te zetten naar een factuur
def generate_invoice(order_data):
    # Factuurstructuur aanmaken
    invoice_data = {
        "company": order_data["company"],
        "customer": order_data["customer"],
        "invoice": {
            "number": f"INV-{order_data['invoice']['number']}",
            "date": datetime.datetime.today().strftime("%d-%m-%Y"),
            "items": [],
            "total": "€ 0,00",
        }
    }

    # Prijzen en hoeveelheden berekenen
    subtotal = 0
    for item in order_data["invoice"]["items"]:
        # Aantal en prijs omzetten naar numerieke waarden
        try:
            quantity = int(item["quantity"])  # aantal
            price = float(item["price"].replace("€", "").replace(",", "."))  # prijs per item
        except ValueError:
            quantity = 0
            price = 0.0

        # Totaalprijs per product
        total_price = quantity * price
        invoice_data["invoice"]["items"].append({
            "description": item["description"],
            "quantity": quantity,
            "price": f"€ {price:.2f}",
            "total_price": f"€ {total_price:.2f}"
        })

        # Voeg toe aan het subtotaal
        subtotal += total_price

    # BTW en totaalprijs berekenen
    vat = round_to_nearest_5_cent(subtotal * (BTW_PERCENTAGE / 100))
    total = round_to_nearest_5_cent(subtotal + vat)

    # Factuurtotaal en BTW toevoegen
    invoice_data["invoice"]["total"] = f"€ {total:.2f}"

    return invoice_data

# Functie om de factuur als PDF te genereren
def generate_pdf(invoice_data):
    filename = f"PDF_INVOICE_{invoice_data['invoice']['number']}.pdf"
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter

    # Titel
    c.setFont("Helvetica-Bold", 16)
    c.drawString(220, height - 40, "Factuur")

    # Bedrijf en klantinformatie
    c.setFont("Helvetica", 12)
    c.drawString(30, height - 80, f"Factuurnummer: {invoice_data['invoice']['number']}")
    c.drawString(30, height - 100, f"Datum: {invoice_data['invoice']['date']}")
    c.drawString(30, height - 120, f"Betalingstermijn: 30 dagen na factuurdatum")
    c.drawString(30, height - 140, f"Bankrekening: NL00INGB0000000000")

    c.setFont("Helvetica", 12)
    c.drawString(30, height - 160, f"Bedrijf: {invoice_data['company']['name']}")
    c.drawString(30, height - 180, f"Adres: {invoice_data['company']['address']}")
    c.drawString(30, height - 200, f"E-mail: {invoice_data['company']['email']}")

    c.setFont("Helvetica", 12)
    c.drawString(30, height - 220, f"Klantennaam: {invoice_data['customer']['name']}")
    c.drawString(30, height - 240, f"Adres: {invoice_data['customer']['address']}")

    # Tabelkopjes
    c.setFont("Helvetica-Bold", 12)
    c.drawString(30, height - 270, "Omschrijving")
    c.drawString(300, height - 270, "Aantal")
    c.drawString(400, height - 270, "Prijs per eenheid")
    c.drawString(500, height - 270, "Totaalprijs")

    y_position = height - 290
    c.setFont("Helvetica", 12)

    for item in invoice_data["invoice"]["items"]:
        c.drawString(30, y_position, item["description"])
        c.drawString(300, y_position, str(item["quantity"]))
        c.drawString(400, y_position, f"€ {item['price']}")
        c.drawString(500, y_position, f"€ {item['total_price']}")
        y_position -= 20

    # Totaalbedragen
    c.setFont("Helvetica-Bold", 12)
    c.drawString(400, y_position - 10, f"Subtotaal: € {invoice_data['invoice']['total']}")
    c.drawString(400, y_position - 30, f"BTW: € {round_to_nearest_5_cent(vat):.2f}")
    c.drawString(400, y_position - 50, f"Totaal: € {invoice_data['invoice']['total']}")

    # PDF opslaan
    c.save()
    print(f"Factuur PDF gegenereerd: {filename}")

# Laad de order JSON uit een bestand
def load_order_json(filename):
    with open(filename, 'r') as file:
        return json.load(file)

# Hoofdfunctie
def main():
    # Laad de orderdata vanuit het JSON-bestand
    order_json_filename = 'order_data.json'  # Het pad naar je JSON-bestand
    order_data = load_order_json(order_json_filename)

    # Genereer factuurdata
    invoice_data = generate_invoice(order_data)

    # Genereer de factuur als PDF
    generate_pdf(invoice_data)

    print("Factuur succesvol gegenereerd als PDF.")

if __name__ == "__main__":
    main()
