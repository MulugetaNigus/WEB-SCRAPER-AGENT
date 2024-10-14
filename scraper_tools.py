import requests
from bs4 import BeautifulSoup
from langchain.tools import tool

class ScraperTool():
    @tool("Scraper Tool")
    def scrape(url: str):
        """
        Useful tool to scrape a website's full content, use this to learn more about a given URL.
        """

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

        # Fetch the page
        response = requests.get(url, headers=headers)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract all text content from the entire page
            full_text = soup.get_text(separator='\n', strip=True)

            return full_text
        else:
            return "Failed to retrieve the webpage."
