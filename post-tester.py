from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        global postvars
        self.send_response(201)
        self.end_headers()
        postvars = self.rfile.read(int(self.headers.getheader('content-length')))
        self.wfile.write(postvars)
        print self.headers 
        print postvars
server = HTTPServer(('', 8888), Handler)
server.serve_forever()
