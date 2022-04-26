from http.server import BaseHTTPRequestHandler, HTTPServer

host="0.0.0.0"
port=8000

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>A whoami server</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p></p>", "utf-8"))
        self.wfile.write(bytes("<p>Response Headers: %s</p>" % self.headers, "utf-8"))
        self.wfile.write(bits("</body></html>", "utf-8"))

    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        message = "Hello, World! Here is a POST response"
        self.wfile.write(bytes(message, "utf8"))

if __name__== '__main__':
    with HTTPServer((host, port), handler) as server:
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print("server is closing")
            server.shutdown()
    
