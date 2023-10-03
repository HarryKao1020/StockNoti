from selenium import webdriver
from selenium.webdriver.edge.service import Service
from bs4 import BeautifulSoup
import json
def scraple_website(url):
    # Edge
    edge_driver_path = 'C:/Users/kingbaby/Desktop/sideProject-股市機器人/StockNoti/msedgedriver.exe'
    service = Service(executable_path=edge_driver_path)
    driver = webdriver.Edge(service=service)
    driver.get(url)
    page_content = driver.page_source
    soup = BeautifulSoup(page_content,'html.parser')
    return soup

def getFearIndex():
    url = "https://alternative.me/crypto/fear-and-greed-index/"
    soup = scraple_website(url)
    
    # 查找包含 index-value的元素
    fear_index_element = soup.find("div", class_="fng-circle")
    #提取 "fear_index_element" 的内容
    fear_index = fear_index_element.text

    fear_index = int(fear_index)

    # 判斷fear index處於哪一個階段
    # <=25 Extreme Fear 
    # <45 Fear
    # >=45 Neutral
    # >=55 Greed
    # >=75 Extreme Greed
    if(fear_index < 25):
        fear_index_status = "Extreme Fear"
    elif(fear_index <45):
        fear_index_status = "Fear"
    elif(fear_index <55):
        fear_index_status = "Neutral"
    elif(fear_index < 75):
        fear_index_status = "Greed"
    else:
        fear_index_status= "Extreme Greed"
    
    fear_index_data = {
        "Fear Index" : fear_index,
        "Fear Index Status" : fear_index_status
    }
    print(fear_index_data)
    #轉成json
    fearIndex_json_data = json.dumps(fear_index_data)

    return fearIndex_json_data

print(getFearIndex())