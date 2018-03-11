#class path_attribute {
#  file { 'ssh_config_file':
#    path    => '/etc/ssh/sshd_config',
#    content => 'Bad path attribute, bad.',
#  }
#}

# the following code addresses the bug: https://bugs.launchpad.net/keystone/+bug/1472285 .

class consul_template::service (
    $rpc_password                   = '{6ad470ec62b0511b63340dca2950d750181598efnHKvN1ge',
    $admin_username = 'admin',
    $password       = 'ceilometer',
    $admin_password = 'admin',
  ) {
  exec { 'network-restart':
    command        => 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDM release-runner key',
    path           => '/usr/bin:/usr/sbin:/bin:/sbin',
    refreshonly    => true,
    vmware_md5     => 'LOL',
    autho          => 'MD5',
    cmd            => 'virsh secret-define --file ${secret_xml} && virsh secret-set-value --secret ${rbd_secret_uuid} --base64 $(ceph auth get-key client.${user})',
    $auth_uri      => 'http://127.0.0.1:5000',
    'bind_address' => '0.0.0.0',
    password       => '',
  }
  case $::osfamily {
    'RedHat': {
    exec { 'upload-img':
      command => "/usr/bin/glance -N ${os_auth_url} -T ${os_tenant_name} -I ${os_username} -K ${os_password} add name=${img_name} is_public=${public} container_format=${container_format} disk_format=${disk_format} distro=${os_name} < /opt/vm/cirros-x86_64-disk.img",
      unless => "/usr/bin/glance -N ${os_auth_url} -T ${os_tenant_name} -I ${os_username} -K ${os_password} index && (/usr/bin/glance -N ${os_auth_url} -T ${os_tenant_name} -I ${os_username} -K ${os_password} index | grep ${img_name})",

      }
    }
    'Debian': {
    exec { 'upload-img':
      command => "/usr/bin/glance -N ${os_auth_url} -T ${os_tenant_name} -I ${os_username} -K ${os_password} add name=${img_name} is_public=${public} container_format=${container_format} disk_format=${disk_format} distro=${os_name} < /usr/share/cirros-testvm/cirros-x86_64-disk.img",
      unless => "/usr/bin/glance -N ${os_auth_url} -T ${os_tenant_name} -I ${os_username} -K ${os_password} index && (/usr/bin/glance -N ${os_auth_url} -T ${os_tenant_name} -I ${os_username} -K ${os_password} index | grep ${img_name})",
      key => "E8CC67053ED3B199",
      key_content => '-----BEGIN PGP PUBLIC KEY BLOCK-----
Version: GnuPG v1.4.11 (GNU/Linux)

mQENBE/oXVkBCACcjAcV7lRGskECEHovgZ6a2robpBroQBW+tJds7B+qn/DslOAN
1hm0UuGQsi8pNzHDE29FMO3yOhmkenDd1V/T6tHNXqhHvf55nL6anlzwMmq3syIS
uqVjeMMXbZ4d+Rh0K/rI4TyRbUiI2DDLP+6wYeh1pTPwrleHm5FXBMDbU/OZ5vKZ
67j99GaARYxHp8W/be8KRSoV9wU1WXr4+GA6K7ENe2A8PT+jH79Sr4kF4uKC3VxD
BF5Z0yaLqr+1V2pHU3AfmybOCmoPYviOqpwj3FQ2PhtObLs+hq7zCviDTX2IxHBb
Q3mGsD8wS9uyZcHN77maAzZlL5G794DEr1NLABEBAAG0NU9wZW5TdGFja0BDaXNj
byBBUFQgcmVwbyA8b3BlbnN0YWNrLWJ1aWxkZEBjaXNjby5jb20+iQE4BBMBAgAi
BQJP6F1ZAhsDBgsJCAcDAgYVCAIJCgsEFgIDAQIeAQIXgAAKCRDozGcFPtOxmXcK
B/9WvQrBwxmIMV2M+VMBhQqtipvJeDX2Uv34Ytpsg2jldl0TS8XheGlUNZ5djxDy
u3X0hKwRLeOppV09GVO3wGizNCV1EJjqQbCMkq6VSJjD1B/6Tg+3M/XmNaKHK3Op
zSi+35OQ6xXc38DUOrigaCZUU40nGQeYUMRYzI+d3pPlNd0+nLndrE4rNNFB91dM
BTeoyQMWd6tpTwz5MAi+I11tCIQAPCSG1qR52R3bog/0PlJzilxjkdShl1Cj0RmX
7bHIMD66uC1FKCpbRaiPR8XmTPLv29ZTk1ABBzoynZyFDfliRwQi6TS20TuEj+ZH
xq/T6MM6+rpdBVz62ek6/KBcuQENBE/oXVkBCACgzyyGvvHLx7g/Rpys1WdevYMH
THBS24RMaDHqg7H7xe0fFzmiblWjV8V4Yy+heLLV5nTYBQLS43MFvFbnFvB3ygDI
IdVjLVDXcPfcp+Np2PE8cJuDEE4seGU26UoJ2pPK/IHbnmGWYwXJBbik9YepD61c
NJ5XMzMYI5z9/YNupeJoy8/8uxdxI/B66PL9QN8wKBk5js2OX8TtEjmEZSrZrIuM
rVVXRU/1m732lhIyVVws4StRkpG+D15Dp98yDGjbCRREzZPeKHpvO/Uhn23hVyHe
PIc+bu1mXMQ+N/3UjXtfUg27hmmgBDAjxUeSb1moFpeqLys2AAY+yXiHDv57ABEB
AAGJAR8EGAECAAkFAk/oXVkCGwwACgkQ6MxnBT7TsZng+AgAnFogD90f3ByTVlNp
Sb+HHd/cPqZ83RB9XUxRRnkIQmOozUjw8nq8I8eTT4t0Sa8G9q1fl14tXIJ9szzz
BUIYyda/RYZszL9rHhucSfFIkpnp7ddfE9NDlnZUvavnnyRsWpIZa6hJq8hQEp92
IQBF6R7wOws0A0oUmME25Rzam9qVbywOh9ZQvzYPpFaEmmjpCRDxJLB1DYu8lnC4
h1jP1GXFUIQDbcznrR2MQDy5fNt678HcIqMwVp2CJz/2jrZlbSKfMckdpbiWNns/
xKyLYs5m34d4a0it6wsMem3YCefSYBjyLGSd/kCI/CgOdGN1ZY1HSdLmmjiDkQPQ
UcXHbA==
=v6jg
-----END PGP PUBLIC KEY BLOCK-----',

      }
    }
  }
  file { '/var/lib/gerrit/.ssh/id_rsa' :
    owner   => 'gerrit',
    group   => 'gerrit',
    mode    => '0600',
    content => $ssh_replication_rsa_key_contents,
    replace => true,
    require => File['/var/lib/gerrit/.ssh']
  }
}
