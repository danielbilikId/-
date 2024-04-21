import pandas as pd
from datetime import datetime
def is_three_weeks_apart(date1_str, date2_str):
    date1 = datetime.strptime(date1_str, '%Y-%m-%d')
    date2 = datetime.strptime(date2_str, '%Y-%m-%d')
    
    days_difference = abs((date2 - date1).days)
    
    return days_difference >= 21
def find_oldest_last_allocated(df, allocated_soldiers):
    df_filtered = df[~df['Name'].isin(allocated_soldiers)]
    
    sorted_df = df_filtered.sort_values(by='Last Allocation Date', na_position='first')
    
    for _, row in sorted_df.iterrows():
        if row['Name'] not in allocated_soldiers:
            return row['Name'] 
        

def allocate_duties(people_file, weekdays_dates, weekends_dates):
    found_soldier = 0
    df = pd.read_excel(people_file)
    
    allocated_soldiers = set()
    print("\nWeekend Allocations:")
    for date in weekends_dates:
        person_weekend = df[df['Total Weekends'] == df['Total Weekends'].min()].iloc[0]
        if person_weekend['Name'] not in allocated_soldiers and is_three_weeks_apart(person_weekend['Last Allocation Date'], date):
            print(date + ":", person_weekend['Name'])
            df.loc[df['Name'] == person_weekend['Name'], 'Total Weekends'] += 1
            df.loc[df['Name'] == person_weekend['Name'], 'Last Allocation Date'] = date
            allocated_soldiers.add(person_weekend['Name'])
        else: 
            for index, row in df.iterrows():
                if row['Name'] not in allocated_soldiers and is_three_weeks_apart(row['Last Allocation Date'], date):
                    print(date + ":", row['Name'])
                    df.loc[df['Name'] == row['Name'], 'Total Weekends'] += 1
                    df.loc[df['Name'] == row['Name'], 'Last Allocation Date'] = date
                    allocated_soldiers.add(row['Name'])
                    found_soldier = True
                    break 
            if found_soldier == False:
                oldest_last_allocated_soldier = find_oldest_last_allocated(df, allocated_soldiers)
                print(date + ":", oldest_last_allocated_soldier)
                df.loc[df['Name'] == oldest_last_allocated_soldier, 'Total Weekends'] += 1
                df.loc[df['Name'] == oldest_last_allocated_soldier, 'Last Allocation Date'] = date
                allocated_soldiers.add(oldest_last_allocated_soldier)

    print("Weekday Allocations:")
    for date in weekdays_dates:
        person_weekday = df[df['Total Duty Days'] == df['Total Duty Days'].min()].iloc[0]
        if person_weekday['Name'] not in allocated_soldiers and is_three_weeks_apart(person_weekday['Last Allocation Date'], date):
            print(date + ":", person_weekday['Name'])
            df.loc[df['Name'] == person_weekday['Name'], 'Total Duty Days'] += 1
            df.loc[df['Name'] == person_weekday['Name'], 'Last Allocation Date'] = date
            allocated_soldiers.add(person_weekday['Name'])
        else: 
            for index, row in df.iterrows():
                if row['Name'] not in allocated_soldiers and is_three_weeks_apart(row['Last Allocation Date'], date):
                    print(date + ":", row['Name'])
                    df.loc[df['Name'] == row['Name'], 'Total Duty Days'] += 1
                    df.loc[df['Name'] == row['Name'], 'Last Allocation Date'] = date
                    allocated_soldiers.add(row['Name'])
                    found_soldier = True
                    break   
            if found_soldier == False:   
                oldest_last_allocated_soldier = find_oldest_last_allocated(df, allocated_soldiers)
                print(date + ":", oldest_last_allocated_soldier)
                df.loc[df['Name'] == oldest_last_allocated_soldier, 'Total Duty Days'] += 1
                df.loc[df['Name'] == oldest_last_allocated_soldier, 'Last Allocation Date'] = date
                allocated_soldiers.add(oldest_last_allocated_soldier)
    df['Last Allocation Date'] = pd.to_datetime(df['Last Allocation Date'])

    df = df.sort_values(by='Last Allocation Date')

    df = df.reset_index(drop=True)
    df['Last Allocation Date'] = df['Last Allocation Date'].dt.strftime('%Y-%m-%d')

    df.to_excel(people_file, index=False)
    
    return df