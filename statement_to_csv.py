## PULLED FROM GOOGLE SHEETS API QUICKSTART

from __future__ import print_function

import os
import csv
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = "1y3tv2tQB9bNBCungTh_Zb3zK2yUMPGEG9YQDi0qpDUM"
SAMPLE_RANGE_NAME = 'Top 100 - Lowest Acceptance Rate!A3:M102'


def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range=SAMPLE_RANGE_NAME).execute()
        values = result.get('values', [])

        if not values:
            print('No data found.')
            return

        # Create a directory to store CSV files
        if not os.path.exists('csv_files'):
            os.makedirs('csv_files')

        for row in values:
            if len(row) >= 5:
                value_in_column_a = row[0]
                value_in_column_e = row[4]
                if value_in_column_a and value_in_column_e:
                    # Generate a CSV file name based on the value in column A
                    csv_file_name = os.path.join('csv_files', f'{value_in_column_a}.csv')
                    # Write the value from column E to the CSV file
                    with open(csv_file_name, 'w', newline='', encoding='utf-8') as csv_file:
                        csv_writer = csv.writer(csv_file)
                        csv_writer.writerow([value_in_column_e])

        print('CSV files created.')

    except HttpError as err:
        print(err)

if __name__ == '__main__':
    main()
