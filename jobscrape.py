import requests
from bs4 import BeautifulSoup

URL = 'https://www.monster.com/jobs/search/?q=Software-Developer'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='ResultsContainer')
job_elem = results.find_all('section', class_='card-content')
for job_elem in job_elem:
    company_title = job_elem.find('h2', class_='title')
    name = job_elem.find('div', class_='company')
    location = job_elem.find('div', class_='location')
    if None in (company_title, name, location):
        continue
    print(company_title.text.strip())
    print(name.text.strip())
    print(location.text.strip())
    print()
