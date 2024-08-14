### 0-world_wide_web
- Displays information about a domain's subdomain.
- Takes 2 command line arguments: the first is the domain (mandatory) and the
  second one is the subdomain (optional). If only the domain is provided, the
  script displays information about four specific subdomains (www, lb-01,
  web-01, web-02). If both the domain and the subdomain is provided then the
  script displays information about that specific subdomain of that domain.
### 1-haproxy_ssl_termination
- Contains haproxy config file.
### 100-redirect_http_to_https
- haproxy config file that configures haproxy to redirect http traffic to https
  with a 301 return code (permanent redirect)
