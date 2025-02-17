from functions import get_field, get_hotel_field, get_supplier_field
import json
import ast

with open("card_example.json", "r", encoding="utf-8") as file:
    data = json.load(file)

with open("hotel.json", "r", encoding="utf-8") as file:
    hotel_data = json.load(file)

with open("suppliers.json", "r",encoding="utf-8") as file:
    supplier_data = json.load(file)

po_number = get_field(data, "po_number")
project = get_field(data, "project").strip('[,],"')
hotel = get_field(data, "hotel").strip('[,],"')
supplier = get_field(data, "select_supplier").strip('[,],"')
currency = get_field(data, "awarded_currency")
awarded_value = get_field(data, "awarded_value")
category = get_field(data, "category")
delivery_date = get_field(data, "delivery_date")
payment_term = get_field(data, "payment_term")
quote_reference = get_field(data, "quote_reference")
shipping_terms = get_field(data, "shipping_terms")
issue_date = get_field(data, "issue_date")
discipline = get_field(data, "discipline")
#supporting_documents = get_field(data, "supporting_documents")

# Get products
product_string = get_field(data, "product_s")
product_list = ast.literal_eval(product_string)

# Hotel details
hotel_name = get_hotel_field(hotel_data, "company_name")
hotel_address = get_hotel_field(hotel_data, "hotel_address")
registered_address = get_hotel_field(hotel_data, "registered_address")
registration_number = get_hotel_field(hotel_data, "registration_no")

# Supplier details
supplier_name = get_supplier_field(supplier_data, "supplier_name")
supplier_address = get_supplier_field(supplier_data, "supplier_address")