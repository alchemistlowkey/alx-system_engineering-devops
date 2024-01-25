# Change the OS configuration for holberton user login

exec { 'update_user_limits_5':
  command  => 'sudo sed -i "s/nofile 5/nofile 50000/" /etc/security/limits.conf',
  provider => shell,
}

exec { 'update_limits':
  command  => 'sudo sed -i "s/nofile 4/nofile 40000/" /etc/security/limits.conf',
  provider => shell,
  require  => Exec['update_user_limits_5']
}
