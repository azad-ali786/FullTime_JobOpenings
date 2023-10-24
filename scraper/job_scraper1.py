import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urlparse, parse_qs

search_query = 'site:lever.co OR site:greenhouse.io "Software Engineering Intern"'

# Define the number of pages of search results to retrieve
num_pages = 1

job_data = []  # List of jobs
for page in range(num_pages):
    google_search_url = f"https://www.google.com/search?q={search_query}&start={page * 10}"

    response = requests.get(google_search_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        search_results = soup.find_all("a", href=True)

        greenhouse_pattern = re.compile(r'https?://boards\.greenhouse\.io/')
        lever_pattern = re.compile(r'https?://jobs\.lever\.co/')

        for link in search_results:
            url = link['href']
            if greenhouse_pattern.search(url):
                parsed_url = urlparse(url)
                actual_url = parse_qs(parsed_url.query).get('q', [''])[0]
                if "jobs" in actual_url:
                    response = requests.get(actual_url)
                    if response.status_code == 200:
                        soup = BeautifulSoup(response.text, "html.parser")
                        job_title_element = soup.find("h1", class_="app-title")
                        company_element = soup.find("span", class_="company-name")

                        if job_title_element is not None and company_element is not None:
                            job_role = job_title_element.text.strip()
                            company = company_element.text.strip().replace("at ", "")
                            job_data.append((company, job_role, actual_url))           
            if lever_pattern.search(url):
                parsed_url = urlparse(url)
                actual_url = parse_qs(parsed_url.query).get('q', [''])[0]
                parts = actual_url.split('/')
                job_id = parts[-1]
                if job_id:
                    response = requests.get(actual_url)
                    if response.status_code == 200:
                        soup = BeautifulSoup(response.text, "html.parser")
                        job_title_element = soup.find("h2")

                        if actual_url.split("/")[-1] == "apply":
                            company_element = actual_url.split("/")[-3]
                        else:
                            company_element = actual_url.split("/")[-2]

                        if job_title_element is not None:
                            job_role = job_title_element.text.strip()
                            company = company_element
                            job_data.append((company, job_role, actual_url))

# Reading the existing content of the README.md file
with open('../README.md', 'r') as readme_file:
    existing_content = readme_file.read()

# Creating a string out of job data
new_job_data = "\n".join([f"| {company} | {job_role} | {actual_url} |" for company, job_role, actual_url in job_data])

# Finding the position for inserting the new data (below the table header)
insert_position = existing_content.index("| Employer | Role | URL |\n| --- | --- | --- |") + len("| Employer | Role | URL |\n| --- | --- | --- |")

# Inserting the new job data below the header in the existing content
new_content = existing_content[:insert_position] + "\n" + new_job_data + existing_content[insert_position:]

# Writes the updated content back to the README.md file
with open('../README.md', 'w') as readme_file:
    readme_file.write(new_content)

print("New data written to README.md file.")
