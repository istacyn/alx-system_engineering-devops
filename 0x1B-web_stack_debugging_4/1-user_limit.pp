# Manifest to modify user limits

exec { 'modify_limits_conf':
  command => "sed -i s/'nofile 5'/'nofile 100'/g /etc/security/limits.conf",
  path    => '/bin'
}

exec { 'modify_limits_conf_2':
  command => "sed -i s/'nofile 4'/'nofile 100'/g /etc/security/limits.conf",
  path    => '/bin'
}
