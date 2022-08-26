
import requests
import folium
import socket
from pyfiglet import Figlet
from time import sleep


while True: #бесконечный цикл
    def get_info_by_ip_link(already_ip='127.0.0.1'): #в функции локальный адрес,как аргумент
        try:
            response = requests.get(url=f'http://ip-api.com/json/{already_ip}', timeout=110).json()
            data = {                  # на строчку выше присваеватся локальный адрес к json файлу
                '[IP]': response.get('query'),
                '[Int prov]': response.get('isp'), #узнаём сотовую связь провайдера
                '[Org]': response.get('org'),
                '[Country]': response.get('country'), #страну
                '[City]': response.get('city'),  # город
                '[Region Name]': response.get('regionName'), #регион
                '[Lat]': response.get('lat'), #долгота
                '[Lon]': response.get('lon'), #широта
                '[Status]': response.get('status'), #статус дейспосбоности
                '[url]': response.get('url'),
                '[ZIP]': response.get('zip'),
                }
            for k, v in data.items(): #прописываем построчно
                sleep(0.85)
                print(f'{k} : {v}\n')
            area = folium.Map(location=[response.get('lat'),response.get('lon')])
            area.save(f'{response.get("query")}_{response.get("city")}.html\n')

        except requests.exceptions.ConnectionError :#при плохом соеденении прописиваем исключение
            print('[!] Please check your connection and repeat again!')
    def main_part_of_code():#функция ввода организации
        try:
            preview_text = Figlet(font='slant')
            print(preview_text.renderText('IP_BY_LINK'))
            ip = input("ВВедите название сайта для определения его расопложения\n"
                   "Например-(google):")
            aleready_ip = socket.gethostbyname(str(ip).lower().upper()+'.com')#по доменному имени определяем айпи
            responsed = requests.get(str('http://www.')+ip+str('.com'))



            get_info_by_ip_link(already_ip=aleready_ip)


        except BaseException or socket.gaierror.errno  as error:# при несущуствовании сайта пишем исключение базы данных
            a = '[!] Link is not founded'
            print(a)


    if __name__ == '__main__':
        main_part_of_code()
        print('\n')

