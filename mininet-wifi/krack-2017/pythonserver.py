

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import urlparse, json


PORT_NUMBER = 8080

#This class will handle incoming requests from Browser
class myHandler(BaseHTTPRequestHandler):

    #Handler for the GET request
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        # Send the html message
        parsed_path = urlparse.urlparse(self.path)
        message = '\n'.join([
            'This should be encrypted by the WPA protocol!',
            'CLIENT VALUES:',
            'client_address=%s (%s)' % (self.client_address,
                self.address_string()),
            'command=%s' % self.command,
            'path=%s' % self.path,
            'real path=%s' % parsed_path.path,
            'query=%s' % parsed_path.query,
            'request_version=%s' %self.request_version,
            '',
            'SERVER VALUES:',
            'server_version=%s' % self.server_version,
            'sys_version=%s' % self.sys_version,
            'protocol_version=%s' % self.protocol_version,
            '',
            ])

        self.wfile.write(message)
        return

try:
    #Create a web server and define the handler to manage the incoming request
    server = HTTPServer(('', PORT_NUMBER), myHandler)
    print 'Started httpserver on port ', PORT_NUMBER

    #Wait forever for incoming http requests
    server.serve_forever()

except KeyboardInterrupt:
    print '^C recieved, shutting down the web server'
    server.socket.close()
