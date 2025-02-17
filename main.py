#import json
import pandas as pd
from fpdf import FPDF
#import ast
#import requests
from fastapi import FastAPI, Request, Response, BackgroundTasks
#import functions

api_token = 'eyJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJQaXBlZnkiLCJpYXQiOjE3Mzk3MDU2NzQsImp0aSI6ImVhYWZhYmI2LTFlYmEtNDFhNS1iMzA0LTg4ZmFhMjZiM2Q4ZSIsInN1YiI6MzAxMDE3NDE5LCJ1c2VyIjp7ImlkIjozMDEwMTc0MTksImVtYWlsIjoiamFzb25AZHlkeC5kaWdpdGFsIn19.crOxwf8adrGCZ5vBtjNPut0pqtf1A-E851SCRdOqjMRPq34HIK-XBC6_DLiy0B8mswJlVsL1c1Yp9nkS8pYKrw'

url = "https://pipefy.com/queries"

# Setup headers
headers = {
    'Authorization': f'Bearer {api_token}',
    'Content-Type': 'application/json'
}