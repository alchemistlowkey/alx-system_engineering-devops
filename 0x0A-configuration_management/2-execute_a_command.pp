# Create a manifest that kills a process named killmenow using Puppet

exec { 'pkill killmenow':
  path    => ['/bin', '/usr/bin'],
  command => 'pkill killmenow',
}
