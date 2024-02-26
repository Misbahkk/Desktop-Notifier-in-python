import time 
from plyer import notification
from news_api import get_news



query = input('What kind of news are you interested in? ')
news_items = get_news(query)

ICON_PATH = "small Project/im.jpg"

def truncate_string(s, max_length):
    if len(s) > max_length:
        return s[:max_length-3] + '...'
    return s
for article in news_items['articles']:
    title = title = truncate_string(article['title'], 64)
    description = truncate_string(article['description'], 74)
    notification.notify(
          title= title,
          message = description,
          app_name = 'news notify',
        #   app_icon = ICON_PATH,
          timeout =5
          )
    time.sleep(10)




