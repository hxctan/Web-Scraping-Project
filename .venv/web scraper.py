import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Set up the path to the ChromeDriver
service = Service('C:/Users/thede/OneDrive/Desktop/chromedriver-win64/chromedriver-win64/chromedriver.exe')

# Initialize the WebDriver
driver = webdriver.Chrome(service=service)

# Navigate to the webpage
driver.get('https://oxylabs.io/blog')

# Parse the page content with BeautifulSoup
content = driver.page_source
soup = BeautifulSoup(content, 'html.parser')
driver.quit()  # Close the browser

# Initialize lists to store blog titles and dates
results = []
other_results = []

# Extract blog titles
for a in soup.findAll(attrs={'class': 'blog-card__content-wrapper'}):
    name = a.find('h2')
    if name and name.text not in results:
        results.append(name.text)

# Extract blog dates
for b in soup.findAll(attrs={'class': 'blog-card__date-wrapper'}):
    date = b.find('p')
    if date and date.text not in other_results:
        other_results.append(date.text)

# Ensure the lists are of equal length
min_length = min(len(results), len(other_results))
results = results[:min_length]
other_results = other_results[:min_length]

# Create a DataFrame and save it to a CSV file
df = pd.DataFrame({'Names': results, 'Dates': other_results})
df.to_csv('names.csv', index=False, encoding='utf-8')

print("Scraping completed successfully. Data saved to 'names.csv'.")

##