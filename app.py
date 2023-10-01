
#載入LineBot所需要的模組
from flask import Flask, request, abort
 
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

from app import app

import getStockInfo

app = Flask(__name__)
 
# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('gIS4eSAOyETZv18tiyNcT4ZZ6274L9UuhLjSowpDjuqYf4dFCNB37+saXJfI1FSr85uiKqqrhteAxVCD3Yjalx/4zC3rshDGfm1/xZXIZmf4pFY2HYnRLs3LqbNiJAmBXAIOwCqSEZTqqnzNa8mfkwdB04t89/1O/w1cDnyilFU=')
 
# 必須放上自己的Channel Secret
handler = WebhookHandler('04279870980e7421fbf1b27cc03165c2')

line_bot_api.push_message('U2032ae75254e026706d91546f58b9af1', TextSendMessage(text='你可以開始了'))


# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
 
  
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
 
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
 
    return 'OK'




#訊息傳遞區塊
##### 基本上程式編輯都在這個function #####
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    fear_index= getStockInfo.getFearIndex
    maintenanceMargin = getStockInfo.getMaintenanceMargin
    stock_info_data={**fear_index,**maintenanceMargin}
    message_text = """
        Fear Index: {},
        Fear Index Status: {},
        大盤融資維持率:{}
    """
    formatted_message = message_text.format(stock_info_data["Fear Index"],stock_info_data["Fear Index Status"],stock_info_data["大盤融資維持率"])

    if event.message.text =='a':
        message = TextSendMessage(text=formatted_message)
        line_bot_api.reply_message(event.reply_token,message)


#主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)