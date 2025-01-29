import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_pdf(text):
    if not os.path.exists('PDF_INVOICE'):
        os.makedirs('PDF_INVOICE')

    filename = 'PDF_INVOICE/generated_invoice.pdf'

    c = canvas.Canvas(filename, pagesize=letter)

    c.drawString(100, 750, text)

    c.save()

    print(f'PDF gegenereerd: {filename}')

if __name__ == '__main__':
    user_input = input("Voer de tekst in die je in de PDF wilt hebben: ")
    generate_pdf(user_input)
    
