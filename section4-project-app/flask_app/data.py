from selenium import webdriver
from urllib.request import urlretrieve
import os
import time

path = '/Users/chromedriver' # chromedriver의 절대경로
driver = webdriver.Chrome(path)

SCROLL_PAUSE_TIME = 1


search_list = ['행복한 강아지 짤', '슬픈 강아지 짤', '화난 강아지 짤', '배고픈 강아지 짤', '졸린 강아지 짤','놀란 강아지 짤'] # 검색 리스트
last_img_num = 700 # 크롤링할 이미지 수

for search_name in search_list:
    url = "https://www.google.com/search?q={}&hl=ko&tbm=isch".format(search_name)
    driver.get(url) # url 접속

    last_height = driver.execute_script("return document.body.scrollHeight") #스크롤 높이 가져옴

    while True: # 스크롤 다운 + 결과 더보기 누르는 와일문
        # 끝까지 스크롤 다운
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # 1초 대기를 해야 막힘없이 동작한다.
        time.sleep(SCROLL_PAUSE_TIME)

        # 스크롤 다운 후 스크롤 높이 다시 가져옴
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            try:
                driver.find_element_by_css_selector(".mye4qd").click()
            except:
                print('while error!')
                break
        last_height = new_height

    img_num = 0   
    try:
        while img_num <= last_img_num:
            img_url = driver.find_elements_by_css_selector('.rg_i')[img_num].get_attribute('src') # url 파싱 

            if not os.path.isdir(search_name): # 폴더 없으면 생성
                        os.mkdir(search_name)

            try:
                urlretrieve(img_url, '{}/{}.jpg'.format(search_name, img_num))
            except:
                print('some error!(folder: {}, img_num: {})'.format(search_name, img_num))
                pass
            img_num += 1
    except:
        pass