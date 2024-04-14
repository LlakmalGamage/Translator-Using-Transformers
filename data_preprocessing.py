import pandas as pd
import os

german_file_path="Data_Sets/deu.txt"
spanish_file_path="Data_Sets/data.csv"

# Initialize lists to store German and English data
german_data = []
english_data = []

with open(german_file_path,'r',encoding='utf-8') as file:
    for line in file:
        english,german,_=line.strip().split('\t')
        english_data.append(english)
        german_data.append(german)


# Create a DataFrame using Pandas
df = pd.DataFrame({ 'English': english_data , 'German': german_data})

# Display the first few rows of the DataFrame
print(df[:20])


df_spanish=pd.read_csv(spanish_file_path)

# renaming the names
new_column_names={'english':'English','spanish':'Spanish'}
df_spanish=df_spanish.rename(columns=new_column_names)

print(df_spanish[:10])


# loading the csv file for german data
file_name=f"data_german.csv"

df.to_csv(f"Data_Sets/{file_name}",index=False)
print("DataFrame saved successfully as", file_name)

current_file_path="Data_Sets/data.csv"
new_file_path="Data_Sets/data_spanish.csv"

os.rename(current_file_path,new_file_path)

print("File renamed successfully to", new_file_path)

german_file_path="data_german.csv"
spanish_file_path="data_spanish.csv"

df1=pd.read_csv(german_file_path)
df2=pd.read_csv(spanish_file_path)
