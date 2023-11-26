# Puppet to make changes to our configuration file
exec { 'file':
  path    => 'usr/bin:/bin',
  command => 'file "    IdentityFile ~/.ssh/school\n    PasswordAuthentication no" >> /etc/ssh/ssh_config',
  returns => [0,1],
}
