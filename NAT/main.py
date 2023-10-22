import os
from http.server import BaseHTTPRequestHandler, HTTPServer
import socket
import json
import requests

# Get the IPinfo API key from the environment variable
ipinfo_api_key = os.environ.get('IPINFO_API_KEY')
if ipinfo_api_key is None:
    raise Exception("IPINFO_API_KEY environment variable is not set.")

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            # Get the client's IP address
            client_ip = self.client_address[0]

            # Use IPinfo API to get location information
            ipinfo_url = f"https://ipinfo.io/{client_ip}/json?token={ipinfo_api_key}"
            response = requests.get(ipinfo_url)
            location_data = json.loads(response.text)

            # Get the current date and time
            date_time = os.popen('date').read()

            # Create an HTML response
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            response_html = f"<html><body>"
            response_html += f"<h1>Current Date and Time:</h1>"
            response_html += f"<p>{date_time}</p>"
            response_html += f"<h1>Your IP Address:</h1>"
            response_html += f"<p>{client_ip}</p>"
            response_html += f"<h1>Your Location:</h1>"
            response_html += f"<p>{location_data.get('city', 'N/A')}, {location_data.get('region', 'N/A')}, {location_data.get('country', 'N/A')}</p>"
            response_html += "</body></html>"
            self.wfile.write(response_html.encode())
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Not Found')

def run(server_class=HTTPServer, handler_class=RequestHandler, port=12345):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}...")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
