import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from entries import get_all_entries, get_single_entry, delete_entry, get_entry_by_word, create_entry, update_entry
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

        if len(parsed) == 2:
            ( resource, id ) = parsed

            if resource == "entries":
                if id is not None:
                    response = f"{get_single_entry(id)}"

                else:
                    response = f"{get_all_entries()}"


            elif resource == "moods":
                if id is not None:
                    response = f"{get_single_mood(id)}"

                else:
                    response = f"{get_all_moods()}"


        elif len(parsed) == 3:
                ( resource, key, value ) = parsed

                if key == "q" and resource == "entries":
                    response = get_entry_by_word(value)

        self.wfile.write(response.encode())

    def do_POST(self):
        self._set_headers(201)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)

        # Convert JSON string to a Python dictionary
        post_body = json.loads(post_body)

        # Parse the URL
        (resource, _) = self.parse_url(self.path)

        # Initialize new animal
        # new_animal = None
        # new_employee = None
        # new_location = None

        # Add a new animal to the list. Don't worry about
        # the orange squiggle, you'll define the create_animal
        # function next.
        if resource == "entries":
            new_entry = None
            new_entry = create_entry(post_body)
            self.wfile.write(f"{new_entry}".encode())

    def do_DELETE(self):

        self._set_headers(204)

        (resource, id) = self.parse_url(self.path)


        if resource == "entries":
            delete_entry(id)
        #   elif resource == "moods":
        #     delete_mood(id)

        self.wfile.write("".encode())

    def do_PUT(self):
        self._set_headers(204)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        # Delete a single animal from the list
        if resource == "entries":
            update_entry(id, post_body)

        # Encode the new animal and send in response
        self.wfile.write("".encode())


def main():
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()
