import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from entries import get_all_entries, get_single_entry
from moods import get_all_moods, get_single_mood

class HandleRequests(BaseHTTPRequestHandler):


      def _set_headers(self, status):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

      def do_OPTIONS(self):
          self.send_response(200)
          self.send_header('Access-Control-Allow-Origin', '*')
          self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE')
          self.send_header('Access-Control-Allow-Headers', 'X-Requested-With, Content-Type, Accept')
          self.end_headers()


      def parse_url(self, path):
          path_params = path.split("/")
          resource = path_params[1]

          if "?" in resource:


              param = resource.split("?")[1]  
              resource = resource.split("?")[0]  
              pair = param.split("=")  
              key = pair[0]  
              value = pair[1]  

              return ( resource, key, value )

          else:
              id = None

              try:
                  id = int(path_params[2])
              except IndexError:
                  pass  
              except ValueError:
                  pass  

              return (resource, id)

      def do_GET(self):
          self._set_headers(200)

          response = {}


          parsed = self.parse_url(self.path)

          if len(parsed) == 3:
              ( resource, id ) = parsed

              if resource == "entries":
                  if id is not None:
                      response = f"{get_single_entry(id)}"
                      self.wfile.write(response.encode())
                  else:
                      response = f"{get_all_entries()}"
                      self.wfile.write(response.encode())

              elif resource == "moods":
                    if id is not None:
                        response = f"{get_single_mood(id)}"
                        self.wfile.write(response.encode())
                    else:
                        response = f"{get_all_moods()}"

def main():
  host = ''
  port = 8088
  HTTPServer((host, port), HandleRequests).serve_forever()
