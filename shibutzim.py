from allocate_duties import allocate_duties
from gSheetsAPI import update_google_sheet

people_file = 'people.xlsx'  
weekdays_dates = ['2024-08-08', '2024-08-13', '2024-08-14', '2024-08-18']
weekends_dates = ['2024-08-22', '2024-08-21']

df = allocate_duties(people_file, weekdays_dates, weekends_dates)
update_google_sheet(df)
