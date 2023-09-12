import json
import logging
import time
from fl_rss_links import*
import schedule
import requests
from bs4 import BeautifulSoup
#from fake_useragent import UserAgent

#ua = UserAgent()

categories_list = []
categories_xml_list = []
# получение страницы
def get_data():
    headers = {
        # 'user-agent' : ua.random,
        'user-agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0',
        'accept':
            'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'cookie':
            '__ddg1_=0ywVtzDxGyVKKjGm2sS5; XSRF-TOKEN=j1H7simHMKdPvRgGYva9VWGzZRUEt6tNRCOjFx0h; PHPSESSID=z5znAJ5GVpW7I5C599jGHBmcXGjfjSsRVKVZVdYX; carrotquest_device_guid=9ec7febc-bcd8-457c-8b8b-24909e5586b6; carrotquest_uid=1430290939561119674; carrotquest_auth_token=user.1430290939561119674.53881-61bf205fd2adedf70dea3c48bc.bb86b041290d77bdbd26c0c813d8313720aeab1f99d48d7f; user_device_id=4st55bl94iiv2yoyfeyuqqkkbmmymzln; new_pf0=1; new_pf10=1; hidetopprjlenta=0; cookies_accepted=1; _ga_RD9LL0K106=GS1.1.1688617111.6.0.1688617113.0.0.0; _ga=GA1.1.1069416201.1688167046; mindboxDeviceUUID=67a28b18-0ac4-447c-9d83-0c280c9be3c1; directCrm-session=%7B%22deviceGuid%22%3A%2267a28b18-0ac4-447c-9d83-0c280c9be3c1%22%7D; analytic_id=1688170433433725; carrotquest_realtime_services_key=; carrotquest_closed_part_id=1478100248160112293; carrotquest_realtime_services_transport=wss; _ga_cid=undefined; uechat_3_pages_count=1; uechat_3_first_time=1688617114083; uechat_3_disabled=true'
    }
    useragent = headers['user-agent']

    
    request_managemend = requests.get(management, headers=headers)
    print(request_managemend)
    time.sleep(1)
    
    request_sites = requests.get(dev_sites, headers=headers).text    
    time.sleep(1)
    
    request_designe = requests.get(designe_and_art, headers=headers).text
    time.sleep(1)
    
    request_programming = requests.get(programming, headers=headers).text
    time.sleep(1)
    
    request_optimization_seo = requests.get(optimization_and_seo, headers=headers).text
    time.sleep(1)
    
    request_translates = requests.get(translates, headers=headers)
    time.sleep(1)
    
    request_texts = requests.get(texts, headers=headers)
    time.sleep(1)
    
    request_three_d_graphics = requests.get(three_d_grafics, headers=headers)
    time.sleep(1)
    
    request_photography = requests.get(photography, headers=headers)
    time.sleep(1)
    
    request_audio_and_video = requests.get(audio_and_video, headers=headers)
    time.sleep(1)
    
    request_advertising_and_marketing = requests.get(advertising_and_marketing, headers=headers)
    time.sleep(1)
    
    request_outsourcing_and_consalting = requests.get(outsourcing_and_consalting, headers=headers)
    time.sleep(1)
    
    request_architecture_and_interier = requests.get(architecture_and_interier, headers=headers)
    time.sleep(1)
    
    request_gamedev = requests.get(gamedev, headers=headers)
    time.sleep(1)
    
    request_polygraph = requests.get(polygraph, headers=headers)
    time.sleep(1)
    
    request_animation = requests.get(animation_and_flash, headers=headers)
    time.sleep(1)
    
    request_engineering = requests.get(engineering, headers=headers)
    time.sleep(1)
    
    request_education = requests.get(education_and_consultations, headers=headers)
    time.sleep(1)
    
    request_mobile_app = requests.get(mobile_applications, headers=headers)
    time.sleep(1)
    
    request_networks = requests.get(networks_and_information_systems, headers=headers)
    time.sleep(1)
    
    request_bots = requests.get('https://www.fl.ru/rss/all.xml?subcategory=279&category=5', headers=headers).text
    time.sleep(1)
    
    request_parsing = requests.get('https://www.fl.ru/rss/all.xml?subcategory=280&category=5', headers=headers).text
    time.sleep(1)

    print(request_translates)
    print(request_networks)

    







    
    soup = BeautifulSoup(request_bots, 'xml')
    soup_parsing = BeautifulSoup(request_parsing, 'xml')

    if soup.find('title').text != '403 Forbidden' or soup_parsing.find('title').text != '403 Forbidden':
 
        with open('pages/fl_management.xml', 'w', encoding="utf-8") as file:
            file.write(request_managemend)
        with open('pages/fl_management.xml', 'r', encoding="utf-8") as file:
            req_managemend = file.read()
            categories_xml_list.append(req_managemend)
            
        with open('pages/fl_sites.xml', 'w', encoding="utf-8") as file:
            file.write(request_sites)
        with open('pages/fl_sites.xml', 'r', encoding="utf-8") as file:
            req_sites = file.read()
            categories_xml_list.append(req_sites)
            
        with open('pages/fl_designe.xml', 'w', encoding="utf-8") as file:
            file.write(request_designe)
        with open('pages/fl_designe.xml', 'r', encoding="utf-8") as file:
            req_designe = file.read()
            categories_xml_list.append(req_designe)
            
        with open('pages/fl_programming.xml', 'w', encoding="utf-8") as file:
            file.write(request_programming)
        with open('pages/fl_programming.xml', 'r', encoding="utf-8") as file:
            req_programming = file.read()
            categories_xml_list.append(req_programming)
            
        with open('pages/fl_optimization.xml', 'w', encoding="utf-8") as file:
            file.write(request_optimization_seo)
        with open('pages/fl_optimization.xml', 'r', encoding="utf-8") as file:
            req_optimization = file.read()
            categories_xml_list.append(req_optimization)
            
        with open('pages/fl_translates.xml', 'w', encoding="utf-8") as file:
            file.write(request_translates)
        with open('pages/fl_translates.xml', 'r', encoding="utf-8") as file:
            req_translates = file.read()
            categories_xml_list.append(req_translates)
            
        with open('pages/fl_texts.xml', 'w', encoding="utf-8") as file:
            file.write(request_texts)
        with open('pages/fl_texts.xml', 'r', encoding="utf-8") as file:
            req_texts = file.read()
            categories_xml_list.append(req_texts)
            
        with open('pages/fl_three_d_graphics.xml', 'w', encoding="utf-8") as file:
            file.write(request_three_d_graphics)
        with open('pages/fl_three_d_graphics.xml', 'r', encoding="utf-8") as file:
            req_three_d = file.read()
            categories_xml_list.append(req_three_d)
            
        with open('pages/fl_photo.xml', 'w', encoding="utf-8") as file:
            file.write(request_photography)
        with open('pages/fl_photo.xml', 'r', encoding="utf-8") as file:
            req_photo = file.read()
            categories_xml_list.append(req_photo)
            
        with open('pages/fl_audio_video.xml', 'w', encoding="utf-8") as file:
            file.write(request_audio_and_video)
        with open('pages/fl_audio_video.xml', 'r', encoding="utf-8") as file:
            req_audio_video = file.read()
            categories_xml_list.append(req_audio_video)
            
        with open('pages/fl_advertising_marketing.xml', 'w', encoding="utf-8") as file:
            file.write(request_advertising_and_marketing)
        with open('pages/fl_advertising_marketing.xml', 'r', encoding="utf-8") as file:
            req_marketing = file.read()
            categories_xml_list.append(req_marketing)
        
            
                
 
        
        
        
        with open('fl_parsing.xml', 'w', encoding="utf-8") as file:
            file.write(request_parsing)
        with open('fl_parsing.xml', 'r', encoding="utf-8") as file:
            req_parsing = file.read()
            
        with open('fl_bots.xml', 'w', encoding="utf-8") as file:
            file.write(request_bots)
        with open('fl_bots.xml', 'r', encoding="utf-8") as file:
            req_bots = file.read()

        pages = [req_parsing, req_bots]
        print('Всё в норме')
        logging.critical(f'Все ок {useragent=}')

        return pages

    elif soup.find('title').text == '403 Forbidden' or soup_parsing.find(
            'title').text == '403 Forbidden':

        with open('fl_parsing.xml', 'r', encoding="utf-8") as file:
            req_parsing = file.read()
        with open('fl_bots.xml', 'r', encoding="utf-8") as file:
            req_bots = file.read()

        pages = [req_parsing, req_bots]
        print('файлы не обновились, 403')
        logging.critical(f'файлы не обновились  {useragent=}')

        return pages

    else:

        with open('fl_parsing.xml', 'r', encoding="utf-8") as file:
            req_parsing = file.read()
        with open('fl_bots.xml', 'r', encoding="utf-8") as file:
            req_bots = file.read()

        print('всё пошло не так')
        logging.critical(f"Все пошло не так {useragent=}")
        pages = [req_parsing, req_bots]

        return pages


def main():
    pages = get_data()
    page_parsing = BeautifulSoup(pages[0], 'xml')
    page_bots = BeautifulSoup(pages[1], 'xml')
    tape_parsing = page_parsing.find_all('item')
    tape_bots = page_bots.find_all('item')
    parsing_list = []
    bots_list = []

    # формирование списков со словарями
    for item in tape_parsing:
        total = {
            'title': item.find('title').text,
            'description': item.find('description').text,
            'link': item.find('link').text,
            'date': item.find('pubDate').text
        }
        parsing_list.append(total)

    for item in tape_bots:
        total = {
            'title': item.find('title').text,
            'description': item.find('description').text,
            'link': item.find('link').text,
            'date': item.find('pubDate').text
        }
        bots_list.append(total)

    category_list = [parsing_list, bots_list]

    with open('all.json', 'w', encoding="utf-8") as file:
        json.dump(category_list, file, indent=4, ensure_ascii=False)


def updates():
    schedule.every(1).minutes.do(main)
    while True:
        schedule.run_pending()
        
if __name__=='__main__':
    main()


