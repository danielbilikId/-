import pandas as pd

# Sample data
data = {
    'Name': ['John', 'Alice', 'Bob', 'Emily', 'Moshe', 'Haim', 'Nahum', 'Nishan', 'Nitin', 'Menashe', 'Joshe'],
    'Total Duty Days': [0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
    'Total Weekends': [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
    'Last Allocation Date': [None] * 11  # Initialize with None for no previous allocation
}

# Create a DataFrame
df = pd.DataFrame(data)

# Write the DataFrame to an Excel file
df.to_excel('people.xlsx', index=False)
