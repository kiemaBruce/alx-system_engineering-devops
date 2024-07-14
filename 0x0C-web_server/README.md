### 0-transfer_file
- Transfers a file from client to server.
- Accepts 4 parameters
	- The path to the file to be transferred
	- The IP of the server we want to transfer the file to
	- The username scp connects with
	- The path to the SSH private key that scp uses
- Display Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY if less
  than 3 parameters passed
- scp transfers the file to the user home directory ~/
- Strict host key checking is disabled when using scp
### 1-install_nginx_web_server
- Installs nginx web server.
- Nginx listens on port 80.
-When querying Nginx at its root / with a GET request (requesting a page) using curl, it
returns a page that contains the string Hello World!
- Allows nginx through ufw if ufw is active.
### 2-setup_a_domain_name
- Includes the name of the .tech domain name that was set up.
### 3-redirection
- Configures a new nginx server just like 1-install_nginx_web_server
- Additionaly, it configures your Nginx server so that /redirect_me is
  redirecting to another page.
- The redirection is a "301 Moved Permanently”.
### 4-not_found_page_404
- Configures your Nginx server to have a custom 404 page that contains the string
  Ceci n'est pas une page
- The page returns an HTTP 404 error code
