from allocate_duties import allocate_duties
# Example usage
people_file = 'people.xlsx'  # Path to the Excel file containing the list of people
weekdays_dates = ['2024-09-09', '2024-09-13', '2024-09-14', '2024-09-18']
weekends_dates = ['2024-09-22', '2024-09-21']

# Allocate duties and display the result
df = allocate_duties(people_file, weekdays_dates, weekends_dates)