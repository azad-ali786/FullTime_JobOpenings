import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urlparse, parse_qs

search_query = 'site:lever.co OR site:greenhouse.io "Software Development Engineer"'

# Define the number of pages of search results to retrieve
num_pages = 4 

for page in range(num_pages):
    google_search_url = f"https://www.google.com/search?q={search_query}&start={page * 10}"

    response = requests.get(google_search_url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parsing the Google search results page
        soup = BeautifulSoup(response.text, "html.parser")

        # Finding and extracting search result links
        search_results = soup.find_all("a", href=True)

        # Regular expression pattern to match Lever and Greenhouse links
        greenhouse_pattern = re.compile(r'https?://boards\.greenhouse\.io/')
        lever_pattern = re.compile(r'https?://jobs\.lever\.co/')

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
            if lever_pattern.search(url):
                parsed_url = urlparse(url)
                actual_url = parse_qs(parsed_url.query).get('q', [''])[0]
                response = requests.get(actual_url)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, "html.parser")
                    # Extract job role and company information from the job page
                    job_title_element = soup.find("h2")
                    # Lever uses different URL patterns for job listings and job applications pages (level/company/job_id/apply or level/company/job_id)
                    if actual_url.split("/")[-1] == "apply":
                        company_element = actual_url.split("/")[-3]
                    else:
                        company_element = actual_url.split("/")[-2]

                    if job_title_element is not None:
                        job_role = job_title_element.text.strip()
                        company = company_element
                        print(f"Job Role: {job_role}\nCompany: {company} \nURL: {actual_url}\n")
                    else:
                        continue
    else:
        print(f"Failed to retrieve search results from Google for page {page}.")
