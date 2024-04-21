from allocate_duties import allocate_duties

people_file = 'people.xlsx'  
weekdays_dates = ['2024-12-12', '2024-12-13', '2024-12-14', '2024-12-18']
weekends_dates = ['2024-12-22', '2024-12-21']

df = allocate_duties(people_file, weekdays_dates, weekends_dates)