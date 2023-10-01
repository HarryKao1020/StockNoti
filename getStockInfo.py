from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import json




def scraple_website(url):
    # 設定 Chrome WebDriver 的選項
    chrome_options = webdriver.ChromeOptions()

    #設定頁面的載入策略: 
    #normal-等待整個頁面家載完畢才執行
    #eager-等待dom樹加載完成，放棄圖片...等加載
    chrome_options.page_load_strategy='normal'

    # 禁止圖片加載
    chrome_options.add_argument("--blink-settings=imagesEnabled=false")

    # 设置WebDriver的路径
    # webdriver_path = '/Users/harry/Desktop/stocknotify_linebot'

    #    建一個Chrome實例
    driver = webdriver.Chrome(options=chrome_options)

    # 打开目标URL
    driver.get(url)

    # 等待頁面加载完成的時間
    driver.implicitly_wait(10)

    
    page_content = driver.page_source

    soup = BeautifulSoup(page_content,'html.parser')

    # 關閉chrome
    driver.quit()

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
    #轉成json
    #fearIndex_json_data = json.dumps(fear_index_data)

    return fear_index_data

def getMaintenanceMargin():
    url = "https://www.istock.tw/post/twmarginrequirement"
    soup = scraple_website(url)

    #取頁面的p class=h1 font-bold m-t
    maintenance_margin = soup.find_all("p",class_="h1 font-bold m-t")
    
    #有4筆相同的，我們要的融資維持率在第二筆
    maintenance_margin_text = maintenance_margin[1].text

    maintenance_margin_data={
        "大盤融資維持率": maintenance_margin_text+"%"
    }

    #轉成json
    #maintenance_margin_json_data = json.dumps(maintenance_margin_data,ensure_ascii=False)
    return maintenance_margin_data
    # 查找包含 index-value的元素



print(getFearIndex())
print(getMaintenanceMargin())