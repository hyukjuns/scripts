import urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


def save_to_png(keyword):
    # Webdriver API > Chrome
    driver = webdriver.Chrome()

    driver.get('https://www.naver.com/')
    time.sleep(1)

    # 검색어 입력
    driver.implicitly_wait(5) # 찾을 요소가 나타날때까지 기다림 (timeout 방지), 세션이 처음 생길때 한번만 있어도 됨
    query_in_naver_portal = driver.find_element(By.CSS_SELECTOR, 'input[id="query"]')
    query_in_naver_portal.send_keys(keyword)
    query_in_naver_portal.send_keys(Keys.ENTER)
    
    # 첫번째 사진 선택 > 이미지 창 생성
    driver.implicitly_wait(5)
    click_first_image = driver.find_element(By.CSS_SELECTOR, '.grid_item _fe_image_viewer_focus_target:nth-child(1)')
    click_first_image.click()

    # 첫번째 사진부터 10개 사진 저장 (Next 버튼 활용)
    for i in range(1,11):
        driver.implicitly_wait(5)
        image = driver.find_element(By.CSS_SELECTOR, '#sub_pack > section.sc_new.sp_viewer.type_sub._fe_image_viewer_root.viewer_open > div > div > div.viewer_wrap._fe_image_viewer_wrap > div.viewer_image._fe_image_viewer_main_image > div.image > img')
        image_src = image.get_attribute('src')
        urllib.request.urlretrieve(image_src, f'img-{i}.png')

        btn_next = driver.find_element(By.CSS_SELECTOR, '#sub_pack > section.sc_new.sp_viewer.type_sub._fe_image_viewer_root.viewer_open > div > div > div.viewer_wrap._fe_image_viewer_wrap > div.viewer_header._fe_image_viewer_header > a.btn_move.btn_next._fe_image_viewer_next_button')
        btn_next.click()

if __name__ == "__main__":
    keyword = input('검색 키워드를 입력하세요')
    save_to_png(keyword)





