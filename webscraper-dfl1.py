import requests
from bs4 import BeautifulSoup
import csv
from time import sleep

# List of unique links
unique_links = [
    "https://www.drinksfoodlife.com/raki",
    "https://www.drinksfoodlife.com/sherry-cocktail-grandarmypunch",
    "https://www.drinksfoodlife.com/about",
    "https://www.drinksfoodlife.com/northdumplingindimessquare",
    "https://www.drinksfoodlife.com/amaromontenegro",
    "https://www.drinksfoodlife.com/naturalwine",
    "https://www.drinksfoodlife.com/tealove",
    "https://www.drinksfoodlife.com/besttacosinbk",
    "https://www.drinksfoodlife.com/artandfish",
    "https://www.drinksfoodlife.com/stylish-in-aspen-drinking-rose-at-bonnies",
    "https://www.drinksfoodlife.com/babydaddy",
    "https://www.drinksfoodlife.com/mole",
    "https://www.drinksfoodlife.com/coyoacan",
    "https://www.drinksfoodlife.com/seawolf",
    "https://www.drinksfoodlife.com/naplesbotanicalgardenwelcomesfrida"
]

# Function to scrape text from a URL
def scrape_text_from_url(url):
    try:
        # Fetch the webpage content
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        sleep(.3)
        # Parse the content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract the text
        text = soup.get_text(separator='\n').strip()

        return text
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

# Prepare the CSV file
output_csv = "articles.csv"

# Open the CSV file for writing
with open(output_csv, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    # Write the header
    writer.writerow(["articles"])

    # Iterate over the links and scrape text
    for link in unique_links:
        print(f"Scraping: {link}")
        text = scrape_text_from_url(link)
        if text:
            writer.writerow([text])
            print(f"Successfully scraped and saved text from {link}")
        else:
            print(f"Failed to scrape {link}")
        print("-" * 80)

print(f"Scraping complete! Data saved to {output_csv}")
