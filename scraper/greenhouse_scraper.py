import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urlparse, parse_qs

# Define the search query
search_query = 'site:greenhouse.io "Associate Software Engineer"'

# Create a Google search URL
google_search_url = f"https://www.google.com/search?q={search_query}"

# Send an HTTP GET request to Google
response = requests.get(google_search_url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the Google search results page
    soup = BeautifulSoup(response.text, "html.parser")

    # Find and extract search result links
    search_results = soup.find_all("a", href=True)

    # Regular expression pattern to match Lever and Greenhouse links
    greenhouse_pattern = re.compile(r'https?://boards\.greenhouse\.io/')

    for link in search_results:
        url = link['href']
        # Check if the link is from Lever or Greenhouse
        if greenhouse_pattern.search(url):
            # Extract the actual URL without the query parameters
            parsed_url = urlparse(url)
            actual_url = parse_qs(parsed_url.query).get('q', [''])[0]

            response = requests.get(actual_url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, "html.parser")
                # Extract job role and company information from the job page
                job_title_element = soup.find("h1", class_="app-title")
                company_element = soup.find("span", class_="company-name")

                if job_title_element is not None and company_element is not None:
                    job_role = job_title_element.text.strip()
                    # Remove "at" prefix and trim leading/trailing spaces from the company name
                    company = company_element.text.strip().replace("at ", "")
                    print(f"Job Role: {job_role}\nCompany: {company}\nURL: {actual_url}\n")
                else:
                    continue
else:
    print("Failed to retrieve search results from Google.")
