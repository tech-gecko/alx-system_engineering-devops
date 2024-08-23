# This manifest modifies the limit descriptor file for a user

exec {'replace_limit-hard':
  provider => shell,
  command  => 'sed -i "s/nofile 5/nofile 1048576/" /etc/security/limits.conf',
}

exec {'replace_limit-soft':
  provider => shell,
  command  => 'sed -i "s/nofile 4/nofile 1048576/" /etc/security/limits.conf',
}
