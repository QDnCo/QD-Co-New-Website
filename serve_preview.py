"""Static preview server with HTTP Range support (needed for video in Safari/iOS and for streaming).
Usage: python3 serve_preview.py ROOT PORT [--noindex]"""
import os,re,sys,functools
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
class Handler(SimpleHTTPRequestHandler):
 noindex=False
 def end_headers(self):
  self.send_header('Accept-Ranges','bytes')
  if self.noindex:self.send_header('X-Robots-Tag','noindex, nofollow, noarchive')
  super().end_headers()
 def list_directory(self,path):
  self.send_error(404);return None
 def send_head(self):
  rng=self.headers.get('Range')
  path=self.translate_path(self.path)
  m=re.match(r'bytes=(\d*)-(\d*)$',rng or '')
  if not m or not os.path.isfile(path):return super().send_head()
  size=os.path.getsize(path)
  start=int(m.group(1)) if m.group(1) else max(0,size-int(m.group(2) or 0))
  end=int(m.group(2)) if m.group(1) and m.group(2) else size-1
  end=min(end,size-1)
  if start>end or start>=size:
   self.send_response(416);self.send_header('Content-Range','bytes */%d'%size);self.end_headers();return None
  f=open(path,'rb');f.seek(start);self._left=end-start+1
  self.send_response(206)
  self.send_header('Content-Type',self.guess_type(path))
  self.send_header('Content-Range','bytes %d-%d/%d'%(start,end,size))
  self.send_header('Content-Length',str(self._left))
  self.end_headers();return f
 def copyfile(self,src,dst):
  left=getattr(self,'_left',None)
  if left is None:return super().copyfile(src,dst)
  while left>0:
   b=src.read(min(65536,left))
   if not b:break
   dst.write(b);left-=len(b)
  self._left=None
if __name__=='__main__':
 os.chdir('/')
 root,port=sys.argv[1],int(sys.argv[2]);Handler.noindex='--noindex' in sys.argv
 ThreadingHTTPServer(('127.0.0.1',port),functools.partial(Handler,directory=root)).serve_forever()
