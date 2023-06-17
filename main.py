import requests
from bs4 import BeautifulSoup
import random
from time import sleep
import csv

url = 'https://pointercrate.com/demonlist/{page}'
file = open('geometrydash.csv', 'w', newline='\n')
csv_obj = csv.writer(file)
csv_obj.writerow(['Name', 'Objects', 'Verifier and Creators'])
for page in range(1, 11):
    r = requests.get(url=url.format(page=page))
    text = r.text
    soup = BeautifulSoup(text, 'html.parser')
    title = soup.find('h1', id="demon-heading")
    creator_verifier = soup.find_all('h3')[6]
    idk = soup.find('div', class_='underlined pad flex wrap')
    try:
        objects = idk.find_all('span')[3]
        print(objects.text)
        csv_obj.writerow([title.text, objects.text, creator_verifier.text])
    except IndexError:
        print('website is updating')
        csv_obj.writerow([title.text, 'website is updating', creator_verifier.text])
    sleep(random.randint(7,12))
file.close()

