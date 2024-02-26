import requests
import json
#5490dd781fae4accabe00d13ef05a715

# query = input('What of news are you intrested in? ')


def get_news(query):
    url = f"https://newsapi.org/v2/everything?q={query}&from=2024-01-26&sortBy=publishedAt&apiKey=5490dd781fae4accabe00d13ef05a715"
    r = requests.get(url)

    news = json.loads(r.text)
    return news
# print(news,type(news))
# for article in news['articles']:
#     print(article['title'])
#     print(article['description'])
#     print("---------------------------------------")

