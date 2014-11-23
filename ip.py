import webapp2
import ipaddr

class Default(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(self.request.remote_addr)

class CheckIPVersion(webapp2.RequestHandler):
    def get(self, ip_version):
        self.response.headers['Content-Type'] = 'text/plain'
        ip=ipaddr.IPAddress(self.request.remote_addr, version=ip_version)

        if ip_version == '4':
            self.response.write(isinstance(ip,ipaddr.IPv4Address))
        elif ip_version == '6':
            self.response.write(isinstance(ip,ipaddr.IPv6Address))

class RedirectToHTTPS(webapp2.RequestHandler):
    def get(self, str):
        self.redirect("https://minivi-ip-echo.appspot.com/")
        
application = webapp2.WSGIApplication([
    ('/', Default),
    (r'/isipv(4|6)', CheckIPVersion),
    (r'/(secure|tls|https)', RedirectToHTTPS),
])

