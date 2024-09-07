# import requests
# import pandas as pd
#
# # URL of the CSV file (replace this with the actual URL of the CSV file)
# csv_url = 'https://example.com/path/to/your/file.csv'
#
# # Send a GET request to download the file
# response = requests.get(csv_url)
#
# # Check if the request was successful
# if response.status_code == 200:
#     # Save the content to a file
#     with open('data.csv', 'wb') as file:
#         file.write(response.content)
#     print("CSV file downloaded successfully.")
# else:
#     print(f"Failed to download file. Status code: {response.status_code}")
#
# # Now read and process the CSV file
# # Using pandas to read and parse the CSV file
# df = pd.read_csv('data.csv')
#
# # Print the first few rows to see the structure
# print(df.head())
#
# # Example: Print specific columns from each row
# # Replace 'ColumnName' with the actual column names you're interested in
# for index, row in df.iterrows():
#     print(f"Column1: {row['Column1']}, Column2: {row['Column2']}")
#
