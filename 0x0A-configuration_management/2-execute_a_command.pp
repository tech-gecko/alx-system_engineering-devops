# manifest that kills a process named killmenow.
exec { 'kill_killmenow_process':
  command => 'pkill killmenow',
  path    => '/usr/bin:/bin',
  onlyif  => 'pgrep killmenow',  # Only run the command if the process is running
}
