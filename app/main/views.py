from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_news, get_specific

@main.route('/')
def index():
  
  recent_news = get_news('top-headlines')

  return render_template('index.html', recents = recent_news)

@main.route('/source/bbc')
def search_bbc(source_name):

  source_name = 'bbc-news'

  specific_source = get_specific(source_name)
  title = f'These are only the stories from {source_name}'

  return render_template('specific.html', favourite = specific_source)
