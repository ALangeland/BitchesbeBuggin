import requests
from bs4 import BeautifulSoup
import csv
import os
import urllib
dir_path = os.path.dirname(os.path.realpath(__file__))

headers = {
    'authority': 'www.basetao.com',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://www.basetao.com/index.php',
    'accept-language': 'da-DK,da;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6,zh;q=0.5,ru;q=0.4,it;q=0.3,de;q=0.2,ml;q=0.1,es;q=0.1',
    'cookie': '__utmc=260164382; __utmz=260164382.1634316107.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); csrf_cookie_name=ec83c73ff288847a7ac088f59806c7ab; __utma=260164382.2064118471.1634316107.1636532045.1636622533.17; bt_session=7e4946f3842ee9351454fb159e0303f7; basetao_e=langeland; basetao_t=b046c02da1ec07b8a283f9a6a902625f; __utmb=260164382.36.9.1636623735944',
}

os.chdir(dir_path)
with open('basetao.csv', 'w+', newline='') as csvfile:
    for order_id in range (591198, 591210):
        URL = "https://basetao.com/index/orderphoto/itemimg/" + str(order_id)

        page = requests.get(URL, headers=headers)

        soup = BeautifulSoup(page.content, 'html.parser')

        results = soup.find("div", class_="container container-top60")

        #order_elements = results.find_all("h4", class_="text-center")[0].text
        BaseWriter = csv.writer(csvfile)
        #for y in range(len(results.find_all('img'))): #(Henter alle billeder pr. ordre nr)
        if len(results.find_all('img')) > 0:
            pic_elements = results.find_all('img')[0].get('src')
            BaseWriter.writerow((order_id,pic_elements))



# Læs ordre nr + hent et billede pr. ordre nr + navngiv billedet med ordre nr. og gemme det. 


