### 0-what-is-my-pid
- Displays its own pid.
### 1-list_your_processes
- Lists all running processes including those that might have a TTY.
- Shows the process hierarchy.
### 2-show_your_bash_pid
- Out of all currently running processes, displays only the ones with the word
bash.
- Does this without using grep.
### 3-show_your_bash_pid_made_easy
- Displays the PID, along with the process name, of processes whose name
contain the word bash.
- Uses pgrep.
### 4-to_infinity_and_beyond
- Displays To infinity and beyond indefinitely.
### 5-dont_stop_me_now
- Stops 4-to_infinity_and_beyond process.
- Sends SIGTERM signal with the kill command.
### 6-stop_me_if_you_can
- Stops 4-to_infinity_and_beyond process using pkill command.
### 7-highlander
- Displays:
	- To infinity and beyond indefinitely.
	- With a sleep 2 in between each iteration.
	- I am invincible!!! when receiving a SIGTERM signal.
### 8-beheaded_process
- Kills the process 7-highlander using SIGKILL signal.
### 100-process_and_pid_file
- Does the following:
	- Creates the file /var/run/myscript.pid containing its PID
	- Displays To infinity and beyond indefinitely
	- Displays I hate the kill command when receiving a SIGTERM signal
	- Displays Y U no love me?! when receiving a SIGINT signal
	- Deletes the file /var/run/myscript.pid and terminates itself when receiving a
	- SIGQUIT or SIGTERM signal
