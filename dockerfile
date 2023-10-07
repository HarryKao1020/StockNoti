# 使用一個基礎映像，你可以根據你的應用程式需求選擇不同的基礎映像
FROM python:3.11

# 設定工作目錄
WORKDIR /app

# 複製應用程式程式碼到容器內
COPY . /app



# 安裝所需的依賴項
RUN pip install -r requirements.txt

# 設定環境變數
# 設定linebot token & secret
ENV LINE_CHANNEL_ACCESS_TOKEN='gIS4eSAOyETZv18tiyNcT4ZZ6274L9UuhLjSowpDjuqYf4dFCNB37+saXJfI1FSr85uiKqqrhteAxVCD3Yjalx/4zC3rshDGfm1/xZXIZmf4pFY2HYnRLs3LqbNiJAmBXAIOwCqSEZTqqnzNa8mfkwdB04t89/1O/w1cDnyilFU='
ENV LINE_CHANNEL_SECRET='04279870980e7421fbf1b27cc03165c2'

# 公開應用程式使用的端口（如果需要）
EXPOSE 8080

# 執行應用程式
CMD ["python", "app.py"]