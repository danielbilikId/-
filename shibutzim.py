from allocate_duties import allocate_duties
# Example usage
people_file = 'people.xlsx'  # Path to the Excel file containing the list of people
weekdays_dates = ['2024-04-01', '2024-04-02', '2024-04-03', '2024-04-04']
weekends_dates = ['2024-04-06', '2024-04-07']

# Allocate duties and display the result
df = allocate_duties(people_file, weekdays_dates, weekends_dates)