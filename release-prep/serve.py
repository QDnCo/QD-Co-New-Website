from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from pathlib import Path
import os
os.chdir(Path(__file__).resolve().parent/'candidate')
class Handler(SimpleHTTPRequestHandler):
 def end_headers(self):
  self.send_header('X-Robots-Tag','noindex, nofollow');super().end_headers()
 def list_directory(self,path):
  self.send_error(404)
ThreadingHTTPServer(('127.0.0.1',8771),Handler).serve_forever()
