# Automate apache configuratiom fix
exec { 'config_file':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path    => '/bin'
}
