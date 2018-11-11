import urllib.request, json
from .models import Article
from .date_pipe import date_calc
article=Article

api_key=None

base_url=None

def configure_request(app):
  global api_key, base_url
  api_key = app.config['NEWS_API_KEY']
  base_url = app.config['NEWS_API_BASE_URL']
  source_base_url = app.config['SOURCE_BASE_URL']

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
  get_specific_url = source_base_url.format(source, api_key)
  print(get_specific_url)
  with urllib.request.urlopen(get_specific_url) as url:
    get_specific_data = url.read()
    get_specific_response = json.loads(get_specific_data)

    news_results = None

    if get_specific_response['articles']:
      news_results_list = get_specific_response['articles']
      news_results = process_results(news_results_list)

  return news_results

def process_results(news_list):
  news_results=[]
  for news_item in news_list:
    info = news_item.get('description')
    headline = news_item.get('title')
    link_to_site = news_item.get('url')
    date_written = news_item.get('publishedAt')
    image = news_item.get('urlToImage')

    daysSince = date_calc(date_written)

    if info:
      info = info
    else:
      info = headline

    if image:
      news_object = Article(info, headline, link_to_site, image, date_written, daysSince)
      news_results.append(news_object)

  return news_results