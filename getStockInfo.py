from selenium import webdriver
from selenium.webdriver.common.by import By
# 设置 Chrome WebDriver 的选项
chrome_options = webdriver.ChromeOptions()

# 禁用图片加载
chrome_options.add_argument("--blink-settings=imagesEnabled=false")

# 设置WebDriver的路径
webdriver_path = '/Users/harry/Desktop/stocknotify_linebot'

# 创建一个Chrome浏览器实例
driver = webdriver.Chrome(options=chrome_options)

# 打开目标URL
url = "https://edition.cnn.com/markets/fear-and-greed"
driver.get(url)

# 等待页面加载完成（你可以根据实际情况调整等待时间）
driver.implicitly_wait(10)

# 查找包含 "fear_index_text" 的元素
fear_index_element = driver.find_element(By.CLASS_NAME,"market-fng-gauge__historical-item-index-value")

#market_situation = driver.find_element(By.CLASS_NAME,"market-fng-gauge__historical-item-index-label:before")
# 提取 "fear_index_text" 的文本内容
fear_index_text = fear_index_element.text

#market_situation_text =market_situation.text
print(fear_index_text)

# 关闭浏览器
driver.quit()

# 从文本内容中提取数字
# previous_close_value = previous_close_text.split(":")[1].strip()

# print("Previous close:", previous_close_value)