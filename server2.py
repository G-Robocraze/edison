import json
from http.server import BaseHTTPRequestHandler, HTTPServer

class Server2Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        json_data = self.rfile.read(content_length)
        data = json.loads(json_data)
        message = data.get('message')
        print('Received message from Server 1: {}'.format(message))
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write('Hello from Server 2'.encode('utf-8'))

server2 = HTTPServer(('localhost', 8081), Server2Handler)
print('Starting Server 2...')
server2.serve_forever()