import urllib.request, json
from .models import Article
article=Article

api_key=None

base_url=None

def configure_request(app):
  global api_key, base_url
  api_key = app.config['NEWS_API_KEY']
  base_url = app.config['NEWS_API_BASE_URL']

def get_news(category):
  get_news_url = base_url.format(category, api_key)
  with urllib.request.urlopen(get_news_url) as url:
    get_news_data = url.read()
    get_news_response = json.loads(get_news_data)

    news_results = None

    if get_news_response['articles']:
      news_results_list = get_news_response['articles']
      news_results = process_results(news_results_list)

  return news_results

def get_specific(source):
  

def process_results(news_list):
  news_results=[]
  for news_item in news_list:
    author = news_item.get('author')
    headline = news_item.get('title')
    link_to_site = news_item.get('url')
    date_written = news_item.get('publishedAt')
    image = news_item.get('urlToImage')

    if image:
      news_object = Article(author, headline, link_to_site, image, date_written)
      news_results.append(news_object)

  return news_results