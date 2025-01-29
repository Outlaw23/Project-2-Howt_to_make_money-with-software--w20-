import json
import math

def round_vat(amount):
    return round(amount, 2)

def generate_invoice(order_json):
    order_data = json.loads(order_json)
    customer = order_data['customer']
    items = order_data['items']
    order_id = order_data['order_id']
    order_date = order_data['order_date']

    subtotal = sum(item['quantity'] * item['unit_price'] for item in items)

    vat_rate = 21

    vat_amount = round_vat(subtotal * vat_rate / 100)
    total = subtotal + vat_amount

    invoice = {
        "invoice_id": f"F{order_id}-{order_date[-4:]}",
        "order_id": order_id,
        "customer": customer,
        "items": [],
        "subtotal": subtotal,
        "vat_rate": vat_rate,
        "vat_amount": vat_amount,
        "total": total,
        "invoice_date": order_date
    }

    for item in items:
        item_total = item['quantity'] * item['unit_price']
        invoice['items'].append({
            "description": item['description'],
            "quantity": item['quantity'],
            "unit_price": item['unit_price'],
            "total": round_vat(item_total)
        })

    return json.dumps(invoice, indent=4)

def process_order(input_file, output_file):
    with open(input_file, 'r') as f:
        order_json = f.read()

    invoice_json = generate_invoice(order_json)

    with open(output_file, 'w') as f:
        f.write(invoice_json)
    
    print(f'Factuur gegenereerd en opgeslagen als {output_file}')

if __name__ == '__main__':
    order_json = '''{
        "order_id": "12345",
        "customer": {
            "name": "John Doe",
            "address": "Mainstreet 123, 1234 AB City",
            "email": "johndoe@example.com"
        },
        "items": [
            {
                "description": "Product A",
                "quantity": 2,
                "unit_price": 50.0
            },
            {
                "description": "Product B",
                "quantity": 1,
                "unit_price": 100.0
            }
        ],
        "order_date": "2025-01-29"
    }'''

    process_order('order.json', 'invoice.json')
