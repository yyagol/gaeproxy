import webapp2
from google.appengine.api import urlfetch

intdomain = "Origin server here FQDN/IP"
extdomain = "External Domain"

class MainPage(webapp2.RequestHandler):
    def get(self):
        try:
           result = urlfetch.fetch(self.request.scheme + "://" + intdomain + self.request.path_qs,payload=None, method=1, headers=self.request.headers)
           if result.status_code == 200:
              content = str(result.content)
              # Uncomment if you want to replace the domain in response body
              #content = content.replace(intdomain,extdomain)
              self.response.headers = result.headers
              self.response.write(content)
           else:
              self.response.status_code = result.status_code
        except urlfetch.Error:
            logging.exception('Caught exception fetching url')

app = webapp2.WSGIApplication([
    ('/.*', MainPage),
], debug=True) 
