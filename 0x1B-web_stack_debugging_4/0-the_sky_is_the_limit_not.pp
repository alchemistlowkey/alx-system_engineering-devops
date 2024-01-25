# Set the ulimit variable to 4096

exec { 'adjust_nginx_Ulimit':
  command => 'sudo sed -i s/15/4096/ /etc/default/nginx',
  path    => ['/bin', '/usr/bin'],
}

# Restart Nginx service
exec {'restart_nginx':
  command => 'sudo service nginx restart',
  path    => ['/bin', '/usr/bin'],
}
