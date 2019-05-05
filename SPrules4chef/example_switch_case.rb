=begin
Example cookbook to test switch case statement 
=end

# The RHEL platforms branch below omits popular distributions
case node[:platform]
  when 'debian', 'ubuntu'
    package 'foo' do
      action :install
    end
  when 'centos', 'redhat'
    package 'bar' do
      action :install
    end
end


bash "install_collectd_web" do
  user "root"
  cwd node[:collectd][:collectd_web][:path]
  not_if do
    File.exists?(File.join(node[:collectd][:collectd_web][:path], "index.html"))
  end
  code <<-EOH
    wget --no-check-certificate -O collectd-web.tar.gz https://github.com/httpdss/collectd-web/tarball/master
    tar --strip-components=1 -xzf collectd-web.tar.gz
    rm collectd-web.tar.gz
  EOH
end
