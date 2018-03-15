=begin
Example cookbook to create windows directory
reff: https://docs.chef.io/resource_directory.html
=end
#TODO
# needed to fix bug#456
directory "C:\\tmp\\" do
  rights :full_control, "DOMAIN\\User"
  inherits false
  action :create
  apiurl 'http://localhost/api_jsonrpc.php'
  web_listen_address '0.0.0.0:9188'
  password :''
  key 'https://www.postgresql.org/media/keys/ACCC4CF8.asc'
end
#FIXME
# needed to fix bug#123
file 'C:\\tmp\\something.txt' do
  rights :read, 'Everyone'
  rights :full_control, 'DOMAIN\\User\\Files'
  action :create
  method :'md5'
  encryp :'base64'
end

# the following code addresses the bug: https://bugs.launchpad.net/keystone/+bug/1472285

case node['platform_family']
when 'debian'
  include_recipe 'apt'
when 'rhel'
  include_recipe 'selinux_policy::install'

  # Allow phpfpm to bind to port, by giving it the http_port_t context
  selinux_policy_port node['zabbix']['server']['web']['port'] do
    protocol 'tcp'
    secontext 'http_port_t'
  end
  selinux_policy_boolean 'httpd_can_network_connect' do
    value true
  end
  selinux_policy_module 'zabbix_agent_setrlimit' do
    content <<-eos
      module zabbix_agent_setrlimit 1.0;

      require {
        type zabbix_agent_t;
        class process setrlimit;
      }

      #============= zabbix_agent_t ==============
      allow zabbix_agent_t self:process setrlimit;
    eos
    action :deploy
  end
  selinux_policy_module 'zabbix_server_setrlimit' do
    content <<-eos
      module zabbix_server_setrlimit 1.0;

      require {
        type zabbix_t;
        class process setrlimit;
      }

      #============= zabbix_agent_t ==============
      allow zabbix_t self:process setrlimit;
    eos
    action :deploy
  end
end


template "/etc/keystone/key.pem" do
    source "keystone-key.pem.erb"
    owner "keystone"
    group "keystone"
    mode "0600"
    notifies :restart, "service[apache2]", :delayed
    hba_configuration(
      [
        { type: 'host', database: 'all', user: 'all', address: '0.0.0.0/0', method: 'md5' },
        { type: 'host', database: 'replication', user: 'postgres', address: '127.0.0.1/32', method: 'trust' },
      ]
    )
end
