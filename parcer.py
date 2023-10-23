import requests
from bs4 import BeautifulSoup


headers = {'user-agent': 'Mozilla/5.0 (Macintosh; '
                         'Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko)'
                         'Chrome/53.0.2785.143 Safari/537.36'

}

dict_data_page_1 = {1:{}}
dict_data_page_2 = {}
dict_data_page_3 = {}
dict_data_page_4 = {}
dict_data_page_5 = {}
dict_data_page_6 = {}
dict_data_page_7 = {}
count_1 = 1
count_dict = 0
for count in range(1, 7):
    url = f'https://scrapingclub.com/exercise/list_basic/?page={count}'

    respons = requests.get(url, headers=headers)

    soup = BeautifulSoup(respons.text, features='html.parser')

    data = soup.find_all('div', class_="w-full rounded border")

    our_dict =[
        dict_data_page_1,
        dict_data_page_2,
        dict_data_page_3,
        dict_data_page_4,
        dict_data_page_5,
        dict_data_page_6,
        dict_data_page_7,
]
    count_dict +=1

    for item in data:
        if count_dict < len(our_dict):
            dictionary = our_dict[count_dict]
            name = item.find('h4').text.replace('\n', '')
            price = item.find('h5').text.replace('\n', '')
            picture = 'https://scrapingclub.com' + item.find('img').get('src')
            url_for_page = 'https://scrapingclub.com' + item.find('a').get('href')
            dictionary.update({count_1: {}})
            dictionary[count_1].update({'name': name})
            dictionary[count_1].update({'price': price})
            dictionary[count_1].update({'picture': picture})
            dictionary[count_1].update({'url': url_for_page})
            count_1 += 1
    count_1 = 1

