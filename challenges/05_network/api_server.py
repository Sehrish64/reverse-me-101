"""Local mock API. Run: python challenges/05_network/api_server.py  (port 8000)"""
import base64
import json
from http.server import BaseHTTPRequestHandler, HTTPServer

TOKEN = base64.b64encode(b"guest:rev-eng-2026").decode()

class H(BaseHTTPRequestHandler):
    def _send(self, code, obj):
        body = json.dumps(obj).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path == "/api/v1/hello":
            self._send(200, {"msg": "hello guest", "docs": "/api/v1/secret"})
        elif self.path == "/api/v1/secret":
            if self.headers.get("X-Auth") == TOKEN:
                self._send(200, {"flag": "RE{the_network_tells_everything}"})
            else:
                self._send(403, {"error": "missing or bad X-Auth header"})
        else:
            self._send(404, {"error": "not found"})

    def log_message(self, *a):
        pass

if __name__ == "__main__":
    print("API on http://127.0.0.1:8000")
    HTTPServer(("127.0.0.1", 8000), H).serve_forever()
