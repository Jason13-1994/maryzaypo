from fpdf import FPDF

def get_field(data, field_id):
    return next(
        (field["value"] for field in data["data"]["card"]["fields"] if field["field"]["id"] == field_id),
        None  # Default to None if not found
    )

def get_hotel_field(data, field_id):
    return next(
        (field["value"] for field in data["data"]["card"]["fields"] if field["field"]["id"] == field_id),
        None  # Default to None if not found
    )

def get_supplier_field(data, field_id):
    return next(
        (field["value"] for field in data["data"]["card"]["fields"] if field["field"]["id"] == field_id),
        None  # Default to None if not found
    )

def general_info(pdf, title, dynamic_data):
    pdf.set_font(family="Arial", size=7, style="B")
    pdf.cell(w=25, h=5, txt=title, border=0)
    pdf.set_font(family="Arial", size=7)
    pdf.cell(w=40, h=5, txt=dynamic_data, border=0)
    pdf.ln(4)
