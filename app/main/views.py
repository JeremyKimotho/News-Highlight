from flask import render_template
from . import main

@main.route('/')
def index():
  
  recent_news = get_news('top-headlines')

  return render_template('index.html', recents = recent_news)