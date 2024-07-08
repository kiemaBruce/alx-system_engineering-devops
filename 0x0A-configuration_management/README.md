### 0-create_a_file.pp
- Creates a file.
- File path is /tmp/school
- File permission is 0744
- File owner is www-data
- File group is www-data
- File contains I love Puppet
## 1-install_a_package.pp
- Installs flask from pip3
- Specific version of flask is 2.1.0.
- Also installs werkzeug version 2.1.1.
## 2-execute_a_command.pp
- Kills a process named killmenow
- Uses the exec puppet resource.
- Uses pkill command.
