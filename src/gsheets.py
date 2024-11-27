import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

def add_to_gsheets(name, what, print_, link):
    scope = ["https://spreadsheets.google.com/feeds"]
    SERVICE_ACCOUNT_FILE = 'creds/credentials.json'

    try:
        creds = ServiceAccountCredentials.from_json_keyfile_name(SERVICE_ACCOUNT_FILE, scope)
        client = gspread.authorize(creds)

        SPREADSHEET_ID = os.getenv('SPREADSHEET_ID')
        sheet = client.open_by_key(SPREADSHEET_ID).get_worksheet(0)

        headers = sheet.row_values(1)

        def find_first_empty_cell(col_idx):
            col_values = sheet.col_values(col_idx)
            return len(col_values) + 1

        max_empty_row = 0
        col_ids = []
        data = []

        if "Дата запроса" in headers:
            date_col_idx = headers.index("Дата запроса") + 1
            col_ids.append(date_col_idx)
            data.append(datetime.today().strftime('%Y-%m-%d'))
            empty_row = find_first_empty_cell(date_col_idx)
            if max_empty_row < empty_row:
                max_empty_row = empty_row

        if "Кто отправил" in headers:
            sender_col_idx = headers.index("Кто отправил") + 1
            col_ids.append(sender_col_idx)
            data.append(name)
            empty_row = find_first_empty_cell(sender_col_idx)
            if max_empty_row < empty_row:
                max_empty_row = empty_row

        if "Название мероприятия" in headers:
            event_col_idx = headers.index("Название мероприятия") + 1
            col_ids.append(event_col_idx)
            data.append(what)
            empty_row = find_first_empty_cell(event_col_idx)
            if max_empty_row < empty_row:
                max_empty_row = empty_row

        if "Печать в типографии" in headers:
            print_col_idx = headers.index("Печать в типографии") + 1
            col_ids.append(print_col_idx)
            data.append("=ИСТИНА" if print_ else "=ЛОЖЬ")

        if "Дизайн" in headers:
            design_col_idx = headers.index("Дизайн") + 1
            col_ids.append(design_col_idx)
            data.append(link)
            empty_row = find_first_empty_cell(design_col_idx)
            if max_empty_row < empty_row:
                max_empty_row = empty_row

        if max_empty_row == 0:
            raise ValueError("row not found")
        for i in range(len(col_ids)):
            sheet.update_cell(max_empty_row, col_ids[i], data[i])
    
    except Exception as e:
        print(f"Error occurred while exporting data to Google Sheets: {e}")