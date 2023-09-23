#puppet
exec { 'kill_killmenow':
    command => 'pkill killmenow',
    path    => '/usr/bin',
    onlyif  => 'pgrep killmenow',
}
