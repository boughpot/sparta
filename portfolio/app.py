import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EA%B3%B5%EC%97%B0&oquery=%EC%A0%84%EC%8B%9C%ED%9A%8C+%EC%86%8C%EA%B0%9C&tqi=hkL%2Btwp0YihsslCmhMGsssssti8-389913',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

displays = soup.select('#main_pack > div.sc_new.cs_common_module.case_list.color_1._cs_perform > div.cm_content_wrap > div > div > div._info > div.list_image_info.type_pure._panel_wrapper > ul:nth-child(1) >li')

for display in displays:
    a = display.select_one('a > div > div.title_box > strong')
    title = a.text
    # date = display.select_one('div.data_area > div > div.info > dl:nth-child(1) > dd').text
    # place = display.select_one('div.data_area > div > div.info > dl:nth-child(2) > dd > a').text
    print(title)
