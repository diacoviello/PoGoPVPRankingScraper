from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import os
import time
#
# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration
chrome_options.add_argument("--no-sandbox")  # Disable sandboxing for headless mode

# Initialize WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Example URL
url = 'https://pvpoke.com/rankings/all/2500/overall/'

# Navigate to the URL
driver.get(url)

# Find the download button
download_button = driver.find_element("css selector", 'a.button.download-csv')

# Click the download button
download_button.click()

# Wait for the file to download
time.sleep(10)  # Adjust the sleep time as needed based on your connection speed

# Assuming the file is downloaded to the default download directory
download_directory = os.path.join(os.path.expanduser("~"), "Downloads")
csv_filename = 'cp2500_all_overall_rankings.csv'
csv_file_path = os.path.join(download_directory, csv_filename)

# Check if file exists and read it
if os.path.exists(csv_file_path):
    print("CSV file downloaded successfully.")
    # Read and process the CSV file
    df = pd.read_csv(csv_file_path)
    print(df.head())
    # Example: Print specific columns from each row
    for index, row in df.iterrows():
        print(f"Column1: {row['Column1']}, Column2: {row['Column2']}")
else:
    print("Failed to download the CSV file.")

# Close the WebDriver
driver.quit()
