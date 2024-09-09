from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Google Sheets authorization
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("C:\\Users\\User\\PycharmProjects\\economy\\economy-434314-5bc46ecfb308.json", scope)
client = gspread.authorize(creds)

# Open your Google Sheet
sheet = client.open("economy").worksheet("aug")

# Function to append data to Google Sheet
def append_to_sheet(income_outcome, category, amount, date):
    sheet.append_row([income_outcome, category, amount, date])
def parse_message(message):
    return ["hii","ho","dfg","gfx"]



app = Flask(__name__)


@app.route("/webhook", methods=["POST"])
def webhook():
    incoming_msg = request.values.get("Body", "").lower()

    # Parse the message here
    parsed_data = parse_message(incoming_msg)  # Implement your own parsing logic
    append_to_sheet(*parsed_data)  # Append the data to Google Sheets

    # Respond to the user
    resp = MessagingResponse()
    resp.message("Transaction logged successfully!")
    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
