from bs4 import BeautifulSoup
import requests

url = 'https://ngs.ru/horoscope/daily/'
page = requests.get(url)
soup = BeautifulSoup(page.text, "lxml")
names = soup.find_all(class_="_4K6U+ _9dcVo")
horoscopes = soup.find_all(class_="BDPZt KUbeq")
horoscope_list = []
name_list = []
for name in names:
    name = name.text
    name_list.append(name)
for horoscope in horoscopes:
    horoscope = horoscope.text
    horoscope_list.append(horoscope)
horoscope_dict = dict(zip(name_list, horoscope_list))
user_input = horoscope_dict[input('Кто вы по гороскопу: ').title()]
print(f'{user_input}')
