"""
Mini logging proxy (HTTP only, local learning use).
Sits between a client and a server and prints every request/response.

    python tools/sniff_proxy.py --listen 8001 --upstream http://127.0.0.1:8000
"""
import argparse
import urllib.request
import urllib.error
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

UPSTREAM = "http://127.0.0.1:8000"

class Proxy(BaseHTTPRequestHandler):
    def do_GET(self):
        print("\n>>> REQUEST")
        print(f"GET {self.path}")
        for k, v in self.headers.items():
            print(f"{k}: {v}")
        req = urllib.request.Request(UPSTREAM + self.path, headers=dict(self.headers))
        try:
            resp = urllib.request.urlopen(req)
        except urllib.error.HTTPError as e:
            resp = e
        body = resp.read()
        print("<<< RESPONSE", resp.status)
        print(body.decode(errors="replace"))
        self.send_response(resp.status)
        self.send_header("Content-Type", resp.headers.get("Content-Type", "text/plain"))
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *a):
        pass

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--listen", type=int, default=8001)
    ap.add_argument("--upstream", default=UPSTREAM)
    a = ap.parse_args()
    UPSTREAM = a.upstream.rstrip("/")
    print(f"Sniffing 127.0.0.1:{a.listen} -> {UPSTREAM}")
    ThreadingHTTPServer(("127.0.0.1", a.listen), Proxy).serve_forever()
