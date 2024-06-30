# Installs version 2.1.0 of flask from pip3 using Puppet.

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

# Installs version 2.1.1 of werkzeug from pip3 using Puppet.

package { 'werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
}
