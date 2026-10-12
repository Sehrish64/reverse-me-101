# Challenge 5: Watch the wire

1. Terminal A: `python challenges/05_network/api_server.py`
2. Terminal B: `python tools/sniff_proxy.py --listen 8001`
3. Terminal C: `python challenges/05_network/app_client.py --api http://127.0.0.1:8001`

The app only prints "Server says: hello guest". But the proxy shows much more.

**Goal:** use what you see in the proxy log to fetch the flag yourself
(curl, Python, anything).

**Lesson:** every app leaks its API, headers and tokens on the network.
This is how real API reverse engineering starts. Only do it on apps and
servers you own or have permission to test.

Note: this is HTTP-only on localhost. Real apps use HTTPS and need more setup.
