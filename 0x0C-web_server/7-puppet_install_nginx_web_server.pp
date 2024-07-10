# This script installs and configures the nginx server using Puppet.

package { 'nginx':
  ensure => 'installed',
}

file { '/var/www/html/index.nginx-debian.html':
  ensure  => 'present',
  content => 'Hello World!',
}

exec { 'sed':
  provider => shell,
  command  => 'sed -i -r "s/^}$/\tlocation \/redirect_me {\n\t\treturn 301 https:\/\/x.com\/IAshimonye83170;\n\t}\n}/" /etc/nginx/sites-available/default',
}

service { 'nginx':
  ensure => 'running',
  enable => true,
}
