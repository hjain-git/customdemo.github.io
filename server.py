from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

PORT = 8787
DIRECTORY = "multilangdemo"

class CustomHandler(SimpleHTTPRequestHandler):
    def translate_path(self, path):
        path = super().translate_path(path)
        if path.endswith("/"):
            path += "multilangdemo_home.html"
        return path

Handler = CustomHandler
httpd = TCPServer(("", PORT), Handler)

print(f"Serving at http://localhost:{PORT}/multilangdemo_home.html")
httpd.serve_forever()
