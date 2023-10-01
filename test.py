import getStockInfo


fear_index= getStockInfo.getFearIndex()
maintenanceMargin = getStockInfo.getMaintenanceMargin()



stock_info_data={**fear_index,**maintenanceMargin}


message_text = """
    Fear Index: {},
    Fear Index Status: {},
    大盤融資維持率:{}
"""

formatted_message = message_text.format(stock_info_data["Fear Index"],stock_info_data["Fear Index Status"],stock_info_data["大盤融資維持率"])

print(formatted_message)