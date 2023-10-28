import urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


# def save_to_png(keyword):

def search_and_save_img(keyword):
    # Webdriver API > Chrome
    driver = webdriver.Chrome()
    driver.get('https://www.naver.com/')

    # 검색어 입력
    driver.implicitly_wait(3) # 찾을 요소가 나타날때까지 기다림 (timeout 방지), 세션이 처음 생길때 한번만 있어도 됨
    query_in_naver_portal = driver.find_element(By.CSS_SELECTOR, 'input[id="query"]')
    query_in_naver_portal.send_keys(keyword)
    query_in_naver_portal.send_keys(Keys.ENTER)

    # 첫번째 사진부터 10개 사진 저장
    for i in range(1,11):
        driver.implicitly_wait(3)
        try:
            image = driver.find_element(By.CSS_SELECTOR, f'#main_pack > section.sc_new.sp_nimage._fe_image_portal_root._prs_img_bas > div > div.image_grid_area._fe_image_portal_list_root > div > div > div:nth-child({i}) > a > img')
            image_src = image.get_attribute('src')
            urllib.request.urlretrieve(image_src, f'img-{i}.png')
        except Exception as e:
            print("페이지에 미리보기 이미지 그리드가 없습니다. \n", e)
            return 

if __name__ == "__main__":
    keyword = input('검색 키워드를 입력하세요 >> ')
    search_and_save_img(keyword)





