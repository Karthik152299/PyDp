import pandas as pd


file_path = r'C:\Users\karth\Downloads\Prob.csv'   


df = pd.read_csv(file_path, encoding='latin1')


print("First few rows of the DataFrame:")
print(df.head())

total_description = df.groupby('description')['value'].sum().reset_index()


print("\nTotal values for each description:")
print(total_description)


total_industry = df.groupby('industry')['value'].sum().reset_index()


print("\nTotal values for each industry:")
print(total_industry)


total_description.to_csv('total_description.csv', index=False)
total_industry.to_csv('total_industry.csv', index=False)

