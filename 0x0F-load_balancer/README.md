### 0-custom_http_response_header
- Configures Nginx server such that all http responses have
a custom header named 'X-Served-By' with a value of the server's hostname.
### 1-install_load_balancer
- Installs and configures HAproxy on your lb-01 server.
- Configures HAproxy so that it send traffic to web-01 and web-02
- Distributes requests using a roundrobin algorithm
