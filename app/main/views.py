from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_news

@main.route('/')
def index():
  
  recent_news = get_news('top-headlines')

  return render_template('index.html', recents = recent_news)