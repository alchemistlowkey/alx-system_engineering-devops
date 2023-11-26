# Puppet to make changes to our configuration file
exec { 'Turn off passwd auth':
  path    => '/etc/ssh/ssh_config',
  command => 'PasswordAuthentication no',
}
exec { 'Declare identity file':
  path    => '/etc/ssh/ssh_config',
  command => 'IdentityFile ~/.ssh/holberton',
}
