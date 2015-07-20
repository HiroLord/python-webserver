import string, cgi, time
from database import *
import json
from os import curdir, sep
from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):

	def do_GET(self):
		try:
			if self.path == '/':
				self.path = "/index.html"
			if self.path[0:3] == '/ws':
				return self.web_service();
			f = open(curdir + sep + self.path)
			self.send_response(200)
			self.send_header('Content-type', 'text/html')
			self.end_headers()
			out = f.read()
			ext = self.path.split('.')
			ext = ext[len(ext)-1]
			if (ext != '.ico'):
				out = bytes(out, 'utf-8')
			self.wfile.write(out)
			f.close()
			return
		except IOError:
			self.send_error(404, 'File Not Found: %s' % self.path)

	def do_POST(self):
		pass

	def web_service(self):
		path = self.path[4:]
		self.send_response(200)
		self.send_header('Content-Type', 'text/json')
		self.end_headers()
		out = sqlGet(path);
		out = json.dumps(out, ensure_ascii=False)
		self.wfile.write(bytes(out, 'utf-8'))
		return
	
def main():
	try:
		server = HTTPServer(('', 80), MyHandler)
		print("Starting server...")
		server.serve_forever()
	except KeyboardInterrupt:
		print(' received, closing server.')
		server.socket.close()

if __name__ == '__main__':
	main()
