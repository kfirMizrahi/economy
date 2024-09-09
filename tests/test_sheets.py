import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Google Sheets authorization
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("/economy-434314-5bc46ecfb308.json", scope)
client = gspread.authorize(creds)

# Open your Google Sheet
sheet = client.open("economy").worksheet("aug")

# Test appending a row
sheet.append_row(["test_income", "test_category", "100", "2024-09-02"])