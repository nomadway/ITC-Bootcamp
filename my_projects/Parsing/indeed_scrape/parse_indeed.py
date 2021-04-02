from bs4 import BeautifulSoup
import requests
import pandas as pd 


def scrape_info(page):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0'}
    url = f'https://ca.indeed.com/jobs?q=data+analyst&l=Toronto&start={page}'
    r = requests.get(url, headers)
    soup = BeautifulSoup(r.content, 'lxml')
    return soup

def transform(soup):
    divs = soup.find_all('div', class_='jobsearch-SerpJobCard')
    for items in divs:
        title = items.find('a').text.strip()
        company = items.find('span', class_='company').text.strip()
        try:
            salary = items.find('span', class_='salaryText').text.strip()
        except:
            salary = ''
        summary = items.find('div', class_='summary').text.strip().replace('\n', '')

        job = {
            'title': title,
            'company': company,
            'salary': salary,
            'summary': summary
        }
        job_list.append(job)
    return

job_list = []
for i in range(0, 40, 10):
    print(f"Getting page, {i}")
    c = scrape_info(0)
    print(len(job_list))

df = pd.DataFrame(job_list)
print(df.head())
df.to_csv('jobs.csv')






























