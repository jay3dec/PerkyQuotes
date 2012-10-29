# accountLookp.py

import os

from google.appengine.ext.webapp import template
from google.appengine.ext.webapp import RequestHandler

class getquotefromtwitter(RequestHandler):
	def get(self):		
		news_rss_url = 'http://search.twitter.com/search.atom?q=perkytweets'
		import feedparser
		info = feedparser.parse(news_rss_url)
		records = info['entries']
		template_values = {"accounts": records};
		path = os.path.join(os.path.dirname(__file__), "templates/main.html")
		self.response.out.write(template.render(path, template_values))
		
