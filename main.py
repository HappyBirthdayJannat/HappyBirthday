import webapp2

class MainPage(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        f = open('index.html', 'r')
        html_data = f.read()
        f.close()
        self.response.write(html_data)

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
