import pandas as pd

data = {
    'Name': ['John', 'Alice', 'Bob', 'Emily', 'Moshe', 'Haim', 'Nahum', 'Nishan', 'Nitin', 'Menashe', 'Joshe'],
    'Total Duty Days': [0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
    'Total Weekends': [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
    'Last Allocation Date': ['2024-01-01'] * 11,  # Initialize with None for no previous allocation
    'Email': ['jhon@gmail.com','Alice@gmail.com','Bob@gmail.com','Emily@gmail.com','Moshe@gmail.com','Haim@gmail.com','Nahum@gmail.com','Nishan@gmail.com','Nitin@gmail.com','Menashe@gmail.com','Joshe@gmail.com']
}

df = pd.DataFrame(data)

df.to_excel('people.xlsx', index=False)
