
#載入LineBot所需要的模組
from flask import Flask, request, abort
 
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

import os
import json

#import getStockInfo

app = Flask(__name__)
 
# 取得token跟secret 
LINE_CHANNEL_ACCESS_TOKEN = os.getenv("LINE_CHANNEL_ACCESS_TOKEN")
LINE_CHANNEL_SECRET = os.getenv("LINE_CHANNEL_SECRET")


# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
 
# 必須放上自己的Channel Secret
handler = WebhookHandler(LINE_CHANNEL_SECRET)
user_id='U2032ae75254e026706d91546f58b9af1'
line_bot_api.push_message(user_id, TextSendMessage(text='你可以開始了'))


def lambda_handler(event, context):
    try:
        # 解析 Lambda 函数的输入事件
        body = json.loads(event['body'])
        signature = event['headers']['X-Line-Signature']
        events = body['events']

        # 验证 Line Bot 事件的签名
        handler.handle(body, signature)

        return {
            'statusCode': 200,
            'body': json.dumps('OK')
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps('Error')
        }

# 監聽所有來自 /callback 的 Post Request
# @app.route("/callback", methods=['POST'])
# def callback():
#     # get X-Line-Signature header value
#     signature = request.headers['X-Line-Signature']
 
  
#     # get request body as text
#     body = request.get_data(as_text=True)
#     app.logger.info("Request body: " + body)
 
#     # handle webhook body
#     try:
#         handler.handle(body, signature)
#     except InvalidSignatureError:
#         abort(400)
 
#     return 'OK'




#訊息傳遞區塊
##### 基本上程式編輯都在這個function #####
@handler.add(MessageEvent, message=TextMessage)
def handler_message(event):

    user_message = event.message.text
    reply_message = "你说的是: " + user_message
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=reply_message))

    #===== 爬蟲＝＝＝＝＝＝＝＝＝
    # if event.message.text =='a':
    #     fear_index= getStockInfo.getFearIndex()
    #     maintenanceMargin = getStockInfo.getMaintenanceMargin()
    #     stock_info_data={**fear_index,**maintenanceMargin}
    #     message_text = """
    #         Fear Index: {},
    #         Fear Index Status: {},
    #         大盤融資維持率:{}
    #     """
    #     formatted_message = message_text.format(stock_info_data["Fear Index"],stock_info_data["Fear Index Status"],stock_info_data["大盤融資維持率"])
    #     message = TextSendMessage(text=formatted_message)
    #     line_bot_api.reply_message(event.reply_token,message)


#主程式
if __name__ == "__main__":
    # 在本地运行时的测试代码
    from flask import Flask, request, abort
    app = Flask(__name__)

    @app.route("/callback", methods=['POST'])
    def callback():
        signature = request.headers['X-Line-Signature']
        body = request.get_data(as_text=True)
        try:
            handler.handle(body, signature)
        except InvalidSignatureError:
            abort(400)
        return 'OK'

    app.run(host='0.0.0.0', port=8080)