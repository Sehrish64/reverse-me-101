"""A tiny 'mobile app' that talks to the API. It only ever says hello."""
import argparse
import base64
import json
import urllib.request

ap = argparse.ArgumentParser()
ap.add_argument("--api", default="http://127.0.0.1:8000")
args = ap.parse_args()

token = base64.b64encode(b"guest:rev-eng-2026").decode()
req = urllib.request.Request(
    args.api + "/api/v1/hello",
    headers={"X-Auth": token, "User-Agent": "RevClient/1.0"},
)
data = json.loads(urllib.request.urlopen(req).read())
print("Server says:", data["msg"])
