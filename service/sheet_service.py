# service/sheet_service.py
import gspread
from google.oauth2.service_account import Credentials

def get_sheet():
    # STEP 1: Auth
    scope = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]
    creds = Credentials.from_service_account_file(
        "mcp_webhook/halogen-honor-465803-e7-3c683c11c53e.json",  # 👈 ใช้ path ที่แท้จริง เช่น "mcp_webhook/keys/service.json"
        scopes=scope
    )

    # STEP 2: Connect
    client = gspread.authorize(creds)

    # STEP 3: เปิด spreadsheet
    spreadsheet_id = "1GgioVsS7e8DGu6LY1mLgjbkspqs_2VfRmElzWxyVZiw"
    spreadsheet = client.open_by_key(spreadsheet_id)
    return spreadsheet.worksheet("Sheet1")  # หรือชื่อ sheet ที่คุณใช้จริง
