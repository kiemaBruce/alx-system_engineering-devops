# kills a process named killmenow
exec { 'kill_killmenow':
  command => '/usr/bin/pkill killmenow',
  onlyif  => '/usr/bin/pgrep killmenow'
}
