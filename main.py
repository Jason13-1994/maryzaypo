import json
import pandas as pd
from fpdf import FPDF
import ast
import requests
from fastapi import FastAPI, Request, Response, BackgroundTasks
import functions

api_token = 'eyJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJQaXBlZnkiLCJpYXQiOjE3Mzk3MDU2NzQsImp0aSI6ImVhYWZhYmI2LTFlYmEtNDFhNS1iMzA0LTg4ZmFhMjZiM2Q4ZSIsInN1YiI6MzAxMDE3NDE5LCJ1c2VyIjp7ImlkIjozMDEwMTc0MTksImVtYWlsIjoiamFzb25AZHlkeC5kaWdpdGFsIn19.crOxwf8adrGCZ5vBtjNPut0pqtf1A-E851SCRdOqjMRPq34HIK-XBC6_DLiy0B8mswJlVsL1c1Yp9nkS8pYKrw'

url = "https://pipefy.com/queries"

# Setup headers
headers = {
    'Authorization': f'Bearer {api_token}',
    'Content-Type': 'application/json'
}

def fn_fetch_card(s_card_id: str = "0") -> ( dict, int ) : # type: ignore
	'''
		Fetch whole card.
	'''
	s_query = functions.fn_tidy(
		'''
			query card{ card(id: ''' + s_card_id + ''' ) {
				id
				url
				pipe { name id }
				fields {
					assignee_values { id name email }
					field { id label }
					array_value
					assignee_values { id }
					value
				}
				current_phase { name id }
				title
			}
		}''' 
	)

@app.post("/get_card/{card_id}")
async def get_card(req: Request, resp: Response, card_id):
	try:
		card, n = my_pipefy.fn_fetch_card( s_card_id = card_id )
		resp.status_code = n
		return card

	except Exception as e:
		resp.status_code = 400
		e.add_note("Assignees_v2 get_card ERROR.")
		return e.__dict__

# Build pdf
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
filename = card_fields.po_number
pdf.add_font("Arial", "", "arial/ARIAL.TTF", uni=True)  # Regular
pdf.add_font("Arial", "B", "arial/ARIALBD 1.TTF", uni=True)  # Bold
# Set the border color to white
pdf.set_draw_color(255, 255, 255)

# Page header
pdf.set_font("Arial", "B", 17)
pdf.set_x(pdf.w - 125 - 10)
pdf.cell(w=50, h=8, txt="PURCHASE ORDER", border=50 , ln=1)
pdf.ln(10)
pdf.set_font(family="Arial", size=14, style="B")
pdf.set_x(pdf.w - 50 - 10)
pdf.cell(w=50, h=8, txt=f"#{card_fields.po_number}", ln=1)
pdf.ln(10)

#columns = ["AWARDED TO:", "COMPANY NAME", "INVOICE DETAILS"]

pdf.set_font("Arial", "B", 7)
pdf.cell(w=90, h=5, txt="AWARDED TO", border=0) #adding text through cells
pdf.cell(w=50, h=5, txt="COMPANY NAME", border=0)
pdf.cell(w=25, h=5, txt="INVOICE DETAILS", border=0)
pdf.ln(4)

# AWARDED TO
pdf.set_font("Arial", "B", 7)
pdf.cell(w=90, h=5, txt=card_fields.supplier_name, border=0)
pdf.cell(w=50, h=5, txt=card_fields.hotel_name, border=0)
pdf.cell(w=25, h=5, txt=card_fields.registered_address, border=0)
pdf.ln(4)


# COMPANY NAME
pdf.cell(w=90, h=5, txt=card_fields.supplier_address, border=0)
pdf.cell(w=50, h=5, txt=card_fields.hotel_address, border=0)
pdf.ln(4)
#pdf.cell(w=60, h=8, txt=columns[1], border=0)
#pdf.cell(w=25, h=8, txt=columns[2], border=0)

pdf.cell(w=90, h=5, txt="", border=0)
pdf.cell(w=50, h=5, txt=card_fields.registration_number, border=0)
pdf.ln(8)

functions.general_info(pdf, "Discipline: ", card_fields.discipline)
functions.general_info(pdf, "Category: ", card_fields.category)
#currency_symbol = card_fields.currency
functions.general_info(pdf, "Award Currency: ",card_fields.currency)
functions.general_info(pdf, "Award Value: ", f"{float(card_fields.awarded_value):,.2f}")
functions.general_info(pdf, "Payment Terms: ", card_fields.payment_term)
functions.general_info(pdf, "Quote Reference: ", card_fields.quote_reference)
functions.general_info(pdf, "Issue Date: ", card_fields.issue_date)
functions.general_info(pdf, "Shipping Term: ", card_fields.shipping_terms)
pdf.ln(4)

pdf.set_draw_color(0, 0, 0)
pdf.set_font("Arial", "B", 7)
pdf.cell(w=10, h=5, txt="#", border=1)
pdf.cell(w=35, h=5, txt="Description", border=1)
pdf.cell(w=17, h=5, txt="UOM", border=1)
pdf.cell(w=17, h=5, txt="QTY", border=1)
pdf.cell(w=25, h=5, txt="Unit Price", border=1)
pdf.cell(w=25, h=5, txt="Total Cost", border=1)
pdf.cell(w=25, h=5, txt="VAT %", border=1)
pdf.cell(w=30, h=5, txt="Total Gross Value", border=1)
pdf.ln(4)

pdf.output(f"{filename}.pdf")