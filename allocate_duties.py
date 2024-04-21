import pandas as pd

def allocate_duties(people_file, weekdays_dates, weekends_dates):
    # Read the Excel file containing the list of people
    df = pd.read_excel(people_file)
    
    # Track allocated soldiers for each day
    allocated_soldiers = set()
    
    # Allocate duties for weekdays
    print("Weekday Allocations:")
    for date in weekdays_dates:
        # Get the next available person for weekday
        person_weekday = df[df['Total Duty Days'] == df['Total Duty Days'].min()].iloc[0]
        # Check if the person is not already allocated for this date and hasn't been allocated this month
        if person_weekday['Name'] not in allocated_soldiers:
            print(date + ":", person_weekday['Name'])
            df.loc[df['Name'] == person_weekday['Name'], 'Total Duty Days'] += 1
            df.loc[df['Name'] == person_weekday['Name'], 'Last Allocation Date'] = date
            allocated_soldiers.add(person_weekday['Name'])
    
    # Allocate duties for weekends
    print("\nWeekend Allocations:")
    for date in weekends_dates:
        # Get the next available person for weekend
        person_weekend = df[df['Total Weekends'] == df['Total Weekends'].min()].iloc[0]
        # If the selected person for the weekend has already been allocated, iterate over all soldiers
        if person_weekend['Name'] not in allocated_soldiers:
            print(date + ":", person_weekend['Name'])
            df.loc[df['Name'] == person_weekend['Name'], 'Total Weekends'] += 1
            df.loc[df['Name'] == person_weekend['Name'], 'Last Allocation Date'] = date
            allocated_soldiers.add(person_weekend['Name'])
        else: 
            for index, row in df.iterrows():
                if row['Name'] not in allocated_soldiers:
                    print(date + ":", row['Name'])
                    df.loc[df['Name'] == row['Name'], 'Total Weekends'] += 1
                    allocated_soldiers.add(row['Name'])
                    break    
    # Update the original Excel file with the updated duty days and weekends done
    df.to_excel(people_file, index=False)
    
    return df

# Example usage
people_file = 'people.xlsx'  # Path to the Excel file containing the list of people
weekdays_dates = ['2024-04-01', '2024-04-02', '2024-04-03', '2024-04-04']
weekends_dates = ['2024-04-06', '2024-04-07']

# Allocate duties and display the result
df = allocate_duties(people_file, weekdays_dates, weekends_dates)
