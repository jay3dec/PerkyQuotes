# main.py

from google.appengine.ext import webapp
from google.appengine.ext.webapp import RequestHandler
from google.appengine.ext.webapp.util import run_wsgi_app
from fetchquote import getquotefromtwitter
	
application = webapp.WSGIApplication([("/", getquotefromtwitter),
                                      ("/fetchquote", getquotefromtwitter),
                                      ],
                                      debug=True)

def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()
