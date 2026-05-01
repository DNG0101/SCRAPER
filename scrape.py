# Import required libraries
import requests              # To send HTTP request
from bs4 import BeautifulSoup  # To parse HTML
import json                  # To save data in JSON format

# Step 1: Define the URL you want to scrape
url = "http://quotes.toscrape.com"

# Step 2: Send GET request to the website
response = requests.get(url)

# Step 3: Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Step 4: Find all quote blocks (each quote is inside class="quote")
quotes_html = soup.find_all("div", class_="quote")

# Step 5: Create an empty list to store extracted data
quotes_data = []

# Step 6: Loop through each quote block and extract data
for quote in quotes_html:
    
    # Extract the quote text
    text = quote.find("span", class_="text").get_text()
    
    # Extract the author name
    author = quote.find("small", class_="author").get_text()
    
    # Store extracted data into dictionary
    quotes_data.append({
        "text": text,
        "author": author
    })

# Step 7: Save the scraped data into a JSON file
with open("quotes.json", "w") as file:
    json.dump(quotes_data, file, indent=4)

# Step 8: Print success message
print("✅ Quotes scraped and saved successfully!")
