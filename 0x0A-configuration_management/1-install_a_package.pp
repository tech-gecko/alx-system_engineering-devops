# Installs version 2.1.0 of flask from pip3 using Puppet

# Ensures the python package is installed
package { 'python3-pip':
  ensure => installed,
}

# Uses the puppet-python module to manage the installation of Flask
python::pip { 'flask':
  ensure       => '2.1.0',
  pip_provider => 'pip3',
}

# Uses the puppet-python module to manage the installation of Werkzeug
python::pip { 'werkzeug':
  ensure       => '2.1.1',
  pip_provider => 'pip3',
}
