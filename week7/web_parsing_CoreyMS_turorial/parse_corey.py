from bs4 import BeautifulSoup
import requests



source = requests.get('https://coreyms.com/').text

soup = BeautifulSoup(source, 'lxml')



for article in soup.find_all('article'):
# article = soup.find('article') #This then should be changed to function. See one line above at 8.

    headline = article.h2.a.text
    print(headline)

    summary = article.find('div', class_='entry-content').p.text
    print(summary)

    video_source = article.find('iframe', class_='youtube-player')['src']

    video_id = video_source.split('/')[4] #index 4 pulls out the id of the video link #
    video_id = video_id.split('?')[0]


    youtube_vid = f'https://youtube.com/watch?vid={video_id}'
    print(youtube_vid)

 
    print()








  