from bs4 import BeautifulSoup
import requests
import csv
import time 
import os 

indeed_pages = [10, 20, 30, 40, 50]

with open ('/home/buranidze/Documents/week7/indeed_scrape/indeed_jobs.csv', 'a', encoding='utf-8', newline='') as f_output:
    csv_print = csv.writer(f_output)

    file_is_empty = os.stat('/home/buranidze/Documents/week7/indeed_scrape/indeed_jobs.csv').st_size == 0
    if file_is_empty:
        csv_print.writerow(['Job_Title', 'Company', 'Location', 'Summary', 'Salary'])

    for pages in indeed_pages: 
        source = requests.get('https://ca.indeed.com/jobs?q=data+analyst&l=Toronto&start={}'.format(pages)).text
        
        soup = BeautifulSoup(source, 'lxml')

        for jobs in soup.find_all(class_='result'):
       
            try:
                title = jobs.h2.text.strip()
            except Exception as e:
                title = None 
            print('Job title: ', title)

            try:
                company = jobs.span.text.strip()
            except Exception as e:
                company = None
            print('Company: ', company)

            try:
                location = jobs.find('span', class_='location').text.strip()
            except Exception as e:
                location = None
            print('Location: ', location)

            try:
                summary = jobs.find('div', class_='summary').text.strip()
            except Exception as e:
                summary = None
            print('Summary: ', summary)

            try:
                salary = jobs.find('span', class_='salary no-wrap').text.strip()
            except Exception as e:
                salary = None
            print('Salary: ', salary)

            
            csv_print.writerow([title, company, location, summary, salary])

            print('-----------------------------------')

            time.sleep(1) #the search will sleep for 1 second before moving to next page#









