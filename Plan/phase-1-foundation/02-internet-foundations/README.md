# 02 - How the Internet Actually Works

This is the hands-on layer for DNS, TCP, HTTP, and the request-response cycle.

## Best implementation ideas
- DNS inspector: resolve a domain and show A, AAAA, and CNAME records
- Raw socket HTTP client: open a TCP connection and send a handcrafted HTTP request
- Request/response tracer: print the exact request line, headers, status code, and response headers
- URL lifecycle lab: start from a URL and trace what happens before the first byte of HTML arrives

## Goal
See the network stack directly instead of only using high-level clients.
