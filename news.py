from newsapi import NewsApiClient
from key import api_key

newsapi = NewsApiClient(api_key=api_key)

def get_articles():
    top_headlines = newsapi.get_everything(q='vazamento de dados')
    return top_headlines['articles']

