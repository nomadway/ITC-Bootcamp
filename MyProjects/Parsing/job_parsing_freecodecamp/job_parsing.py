from bs4 import BeautifulSoup
import requests
import time 

print("Put the skills you are not familier with:")
unfamiliar_skill = input('>')
print(f'Filtering out {unfamiliar_skill}')

def find_jobs():

    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    
    for index, job in enumerate (jobs): 
        published_date = job.find('span', class_='sim-posted').span.text
        if 'few' in published_date: 
            company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '') 
            skills = job.find('span', class_='srp-skills').text.replace(' ', '')
            more_info = job.header.h2.a['href']

            if unfamiliar_skill not in skills: 
                with open(f"jobposts/{index}.txt", 'w')as job_list: 
                    job_list.write(f"Company Name: {company_name.strip()}\n")
                    job_list.write(f"Required Skills: {skills.strip()}\n")
                    job_list.write(f"More Info: {more_info}")
                print(f"File saved: {index}")

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 1 # one minute wait#
        print(f"Wait for {time_wait} minutes...")
        time.sleep(time_wait)
        
        # time.sleep(time_wait * 60)
        