#class path_attribute {
#  file { 'ssh_config_file':
#    path    => '/etc/ssh/sshd_config',
#    content => 'Bad path attribute, bad.',
#  }
#}

class consul_template::service {
  exec { 'network-restart':
    command     => 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDM release-runner key',
    path        => '/usr/bin:/usr/sbin:/bin:/sbin',
    refreshonly => true
  }
}
