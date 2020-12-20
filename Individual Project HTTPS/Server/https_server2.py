import socketserver
import http.server
import ssl
from http.server import HTTPServer, BaseHTTPRequestHandler

class Serv(BaseHTTPRequestHandler):

	def do_GET(self):
		if self.path == '/':
			self.path = 'index.html'
		try:
			file_to_open = open(self.path[1:]).read()
			self.send_response(200)
		except:
			file_to_open = "File not found"
			self.send_response(404)
		self.end_headers()
		self.wfile.write(bytes(file_to_open, 'utf-8'))


httpd = socketserver.TCPServer(('0.0.0.0', 10000), http.server.SimpleHTTPRequestHandler)

httpd.socket = ssl.wrap_socket(httpd.socket, certfile= "/home/naquib/Desktop/individualproject/cert.pem", keyfile= "/home/naquib/Desktop/individualproject/key.pem", server_side=True)

httpd.serve_forever()
