import requests
from bs4 import BeautifulSoup

# Function to fetch webpage content
def fetch_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Ensure successful response
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching the page: {e}")
        return None

# Function to parse and scrape the required data (e.g., news headlines)
def scrape_data(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    headlines = []

    # Adjusted to find headlines on TechCrunch (inside h2 tags with an a tag)
    for item in soup.find_all('h2'):
        headline = item.find('a')
        if headline:
            headlines.append(headline.get_text().strip())

    return headlines

# Function to present the data in a user-friendly format
def display_data(data):
    if data:
        print("\nTop Headlines:")
        for i, headline in enumerate(data, 1):
            print(f"{i}. {headline}")
    else:
        print("No data found.")

# Main function to manage the program flow
def interactive_scraper():
    print("Interactive Web Scraper")
    
    url = input("Enter the URL to scrape: ")
    html_content = fetch_page(url)

    if html_content:
        headlines = scrape_data(html_content)
        display_data(headlines)

# Test the program with TechCrunch
interactive_scraper()
