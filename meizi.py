# -*- coding: utf-8 -*-
import os
import random
import requests
import time
from bs4 import BeautifulSoup


# 定义获取网页内容装饰器
def decorator(get_info):
    def get_info_from_url(url):
        # 获取网页的HTML文档
        html = requests.get(url, headers=Hostreferer)
        # print(html.text)
        # soup全局变量
        global soup
        # 格式化
        soup = BeautifulSoup(html.text, 'html.parser')

        return get_info(url)

    return get_info_from_url


# 获取总页数
@decorator
def get_page_num_info(homepage_url):
    # 获取主页上总页数所在标签的信息
    page_info = soup.find_all('a', class_='page-numbers')
    # print(page_info)
    max_page_num = page_info[-2].text
    # print(max_page_num)
    return max_page_num


# 获取每页24条内容的url
@decorator
def get_url_info(page_url):
    info_list = []
    for info in soup.find('div', class_='postlist').find_all('a', target="_blank"):
        if info.get_text() != '':
            info_list.append(info.get('href'))
    # print(info_list)
    return info_list


# 获取girl的信息
@decorator
def get_girl_info(url):
    pic_page = soup.find_all('span')
    # print(pic_page)
    '''
    页数不足问题：
        页数超过5页，最后一页：pic_page[9].text
        页数不足时，最后一页：pic_page[8].text
    '''
    if pic_page[9].text == '下一页':
        pic_number = pic_page[8].text
    else:
        pic_number = pic_page[9].text

    # 将span标签下有数字内容的放在列表中，取列表的最大值
    # pic_number_list=[]
    # for i in range(10):
    #     if pic_page[i].text.isdigit():
    #         pic_number_list.append(int(pic_page[i].text))
    # pic_number = max(pic_number_list)

    # print(pic_number)
    girl_class = pic_page[1].text[-4:]
    # print(pic_class)
    pic_title_info = soup.find('h2', class_='main-title')
    pic_title = pic_title_info.text
    if pic_title.count('"') >= 1:
        pic_title_2 = pic_title[0:pic_title.find('"')]
    else:
        pic_title_2 = pic_title
    # print(pic_title)
    return girl_class, pic_title, pic_title_2, pic_number


# 获取每张图片的url
@decorator
def get_pic_url_info(url):
    # print(type(soup))
    # 部分页面没有alt=pic_title_2内容
    if soup.find('img', alt=pic_title_2):
        pic_url_info = soup.find('img', alt=pic_title_2)
        #print(pic_url_info)
    else:
        pic_url_info = soup.find('img', alt='')
        #print(pic_url_info)
    pic_url = pic_url_info['src']
    # print(pic_url)
    file_name = pic_url.split(r'/')[-1]
    # print(file_name)
    # time.sleep(random.randint(2, 5) / 10)
    return pic_url, file_name


# 保存图片
def save_image(url):
    html = requests.get(url, headers=Hostreferer)
    file_path = os.path.join(path, 'images', girl_class, pic_title_1, file_name)
    with open(file_path, 'wb') as wstream:
        wstream.write(html.content)


# 处理非法字符
def invaild_symbol_trade(pic_title):
    invaild_symbol = ['/', '\\', '"', ':', '*', '?', '<', '>', '|']
    for symbol in invaild_symbol:
        if symbol in pic_title:
            pic_title = pic_title.replace(symbol, '')
            invaild_symbol_trade(pic_title)
    return pic_title


def file_exists(path, girl_class, pic_title, pic_num):
    file_num = 0
    dir_num = 0
    flag = 0
    global pic_title_1
    pic_title_1 = invaild_symbol_trade(pic_title)
    if not os.path.exists(os.path.join(path, 'images', girl_class)):
        os.mkdir(os.path.join(path, 'images', girl_class))

    if not os.path.exists(os.path.join(path, 'images', girl_class, pic_title_1)):
        os.mkdir(os.path.join(path, 'images', girl_class, pic_title_1))

    file_path = os.path.join(path, 'images', girl_class, pic_title_1)
    for lists in os.listdir(file_path):
        # print(lists)
        if os.path.isfile(os.path.join(file_path, lists)):
            # print('OK')
            file_num += 1
            # print(file_num)
        elif os.path.isdir(os.path.join(file_path, lists)):
            dir_num += 1
    if file_num == int(pic_num):
        file_info = '{}已存在，且下載完成'.format(pic_title)
        log(file_info)
        flag = 1
    # print(flag)
    return flag


def log(info):
    if not os.path.exists(os.path.join(path, 'log')):
        os.mkdir(os.path.join(path, 'log'))
    log_path = os.path.join(path, 'log/log.txt')
    message = '{}:{}\n'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), info)
    with open(log_path, 'a') as wstream:
        wstream.write(message)


homepage_url = 'https://www.mzitu.com'

Hostreferer = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
    'referer': 'https://www.mzitu.com'
}

if __name__ == '__main__':
    path = os.path.dirname(__file__)
    page_num = get_page_num_info(homepage_url)
    # print(page_num)
    for num in range(1, int(page_num) + 1):
        url = '{}/page/{}'.format(homepage_url, num)
        girl_list = get_url_info(url)
        # print(girl_list)
        for list_url in girl_list:
            # print(list_url)
            girl_class, pic_title, pic_title_2, pic_num = get_girl_info(list_url)
            # print(girl_class, pic_title, pic_num)
            flag = file_exists(path, girl_class, pic_title, pic_num)
            time.sleep(random.randint(2, 5) / 10)
            if flag == 0:
                for i in range(1, int(pic_num) + 1):
                    pic_url, file_name = get_pic_url_info('{}/{}'.format(list_url, i))
                    print(pic_url, "下載完成")
                    save_image(pic_url)
                    time.sleep(random.randint(5, 10) / 10)
                    log('第{}頁{}的第{}張圖片{}已下載完成'.format(num, list_url, i, pic_url))
                # else:
                # print('下载完成')