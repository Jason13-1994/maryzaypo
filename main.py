#import json
import pandas as pd
from fpdf import FPDF
#import ast
#import requests
from fastapi import FastAPI, Request, Response, BackgroundTasks
from flask import Flask, request, jsonify
#import functions

pip_org = 300782631
url = "https://pipefy.com/queries"

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    # Get the JSON data from the incoming POST request
    data = request.get_json()

    # Log the received data (you can modify this based on your needs)
    print("Received webhook data:", data)

    # Send a response back
    return jsonify({"status": "success", "message": "Webhook received!"})


api_token = 'eyJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJQaXBlZnkiLCJpYXQiOjE3Mzk3MDU2NzQsImp0aSI6ImVhYWZhYmI2LTFlYmEtNDFhNS1iMzA0LTg4ZmFhMjZiM2Q4ZSIsInN1YiI6MzAxMDE3NDE5LCJ1c2VyIjp7ImlkIjozMDEwMTc0MTksImVtYWlsIjoiamFzb25AZHlkeC5kaWdpdGFsIn19.crOxwf8adrGCZ5vBtjNPut0pqtf1A-E851SCRdOqjMRPq34HIK-XBC6_DLiy0B8mswJlVsL1c1Yp9nkS8pYKrw'

# Setup headers
headers = {
    'Authorization': f'Bearer {api_token}',
    'Content-Type': 'application/json'
}
