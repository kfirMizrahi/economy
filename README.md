# WhatsApp Finance Tracker Chatbot

This project is a WhatsApp chatbot that logs financial transactions (income/outcome, category, amount, and date) to a Google Sheet using Twilio's API for WhatsApp and the Google Sheets API. The bot is hosted on Heroku to run continuously.

## Features
- Log income and expenses through WhatsApp.
- Store data in Google Sheets automatically.
- Easy deployment on Heroku for continuous operation.
  
## Prerequisites

### Accounts Needed:
1. **Google Cloud Account**: To use the Google Sheets API.
2. **Twilio Account**: To enable WhatsApp messaging.
3. **Heroku Account**: To deploy the bot for continuous operation.

### Libraries and Tools:
- `gspread`: To interact with Google Sheets.
- `oauth2client`: To handle Google Sheets authentication.
- `Flask`: To create the webhook for Twilio.
- `Twilio`: To receive and send WhatsApp messages.
- `Heroku CLI`: To deploy your app on Heroku.

## Setup Guide

### Step 1: Setting Up Google Sheets API

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project and enable the **Google Sheets API**.
3. Create a **Service Account** and download the credentials JSON file.
4. Share your Google Sheet with the **service account email** found in the JSON file (`client_email`) and grant **Editor** access.

### Step 2: Setting Up Twilio for WhatsApp

1. Create a [Twilio account](https://www.twilio.com/).
2. Set up the WhatsApp Sandbox in the Twilio Console under **Messaging > Try it Out > Send a WhatsApp Message**.
3. Copy your **Account SID**, **Auth Token**, and WhatsApp-enabled number.

### Step 3: Local Development

1. Clone this repository and navigate to the project directory:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Install the required Python libraries:
    ```bash
    pip install -r requirements.txt
    ```

3. Place the Google Sheets credentials JSON file in the project directory.

4. Update the `app.py` with the correct Google Sheet name.

5. Run the Flask app locally:
    ```bash
    python app.py
    ```

6. Expose the local server using `ngrok` to test with Twilio (optional):
    ```bash
    ngrok http 5000
    ```

### Step 4: Deploy to Heroku

1. Install the Heroku CLI:
    ```bash
    https://devcenter.heroku.com/articles/heroku-cli
    ```

2. Log in to Heroku:
    ```bash
    heroku login
    ```

3. Create a Heroku app:
    ```bash
    heroku create
    ```

4. Push your local project to Heroku:
    ```bash
    git add .
    git commit -m "Initial deployment"
    git push heroku master
    ```

5. Set the webhook URL in Twilio to point to your Heroku app:
    ```
    https://<your-heroku-app>.herokuapp.com/webhook
    ```

6. Check Heroku logs to verify the app is running:
    ```bash
    heroku logs --tail
    ```

### Step 5: Testing

1. Send a WhatsApp message in the following format:
    ```
    income food 50 2024-09-02
    ```
   
2. The message should be logged to your Google Sheet with columns for **Income/Outcome**, **Category**, **Amount**, and **Date**.

## Project Structure

```plaintext
.
├── main.py                 # Flask app that handles incoming WhatsApp messages
├── credentials.json       # Google Sheets API credentials (not included in the repo)
├── requirements.txt       # Python dependencies
├── Procfile               # Defines process for running on Heroku
└── README.md              # Project documentation
```

## Environment Variables

- **GOOGLE_SHEETS_CREDENTIALS**: Path to your Google Sheets API credentials file.
- **TWILIO_ACCOUNT_SID**: Your Twilio Account SID.
- **TWILIO_AUTH_TOKEN**: Your Twilio Auth Token.

## License

This project is licensed under the MIT License.
