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
