# Configure Nginx to handle load more effectively
exec { 'nginx config':
  onlyif   => 'test -e /etc/default/nginx',
  command  => "sed -i s/'-n 15'/'-n 4096'/g /etc/default/nginx; service nginx restart",
  provider => 'shell'
}
