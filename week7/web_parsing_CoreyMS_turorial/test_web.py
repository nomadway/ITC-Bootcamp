from bs4 import BeautifulSoup
import requests

with open('testweb.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

# match = soup.title.text  ##This will only pase the title without tags##
# print(match)

for article in soup.find_all('div', class_='article'):


    headline = article.h2.a.text
    print(headline)

    summary = article.p.text
    print(summary)

    print()




