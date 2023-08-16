import gspread

gc = gspread.service_account(filename='creds.json')


def get_sheet_data(sheet_name: str):
    sheet = gc.open(sheet_name).sheet1
    data = sheet.get_all_records()
    return data


print(get_sheet_data('aboniments'))
