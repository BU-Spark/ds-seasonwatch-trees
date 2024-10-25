# Load the CSV file
import pandas as pd


file_path = '/Users/aditya8chopra/Downloads/alldata.csv'  # Change this to the actual path
df = pd.read_csv(file_path, na_values=['NA', 'na', '', 'NaN'])

missing_all_1 = df.isna().all(axis=1).sum()
print(f'Rows with all values missing (Method 1): {missing_all_1}')

missing_all_2 = df.shape[0] - df.dropna(how='all').shape[0]
print(f'Rows with all values missing (Method 2): {missing_all_2}')

missing_all_3 = df.apply(lambda row: row.isna().all(), axis=1).sum()
print(f'Rows with all values missing (Method 3): {missing_all_3}')

missing_all_4 = df.eq(pd.NA).all(axis=1).sum()
print(f'Rows with all values missing (Method 4): {missing_all_4}')

if missing_all_1 > 0:
    print("Example of a row with all missing values:")
    print(df[df.isna().all(axis=1)].head(1))  # Display first row with all missing values
else:
    print("No rows with all values missing.")