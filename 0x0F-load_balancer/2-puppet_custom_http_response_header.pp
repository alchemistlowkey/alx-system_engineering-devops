#!/usr/bin/env bash
# Automate the task of creating a custom HTTP header response, but with Puppet.
exec { '/usr/bin/env apt-get -y update' : }
-> package { 'nginx':
  ensure => installed,
}

Facter.add('custom_hostname') do
  setcode 'hostname'
end

file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('nginx/default.erb'),
  notify  => Service['nginx'],
}

service { 'nginx':
  ensure  => running,
  enable  => true,
}
