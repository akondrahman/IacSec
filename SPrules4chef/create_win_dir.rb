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
end
#FIXME 
# needed to fix bug#123
file 'C:\\tmp\\something.txt' do
  rights :read, 'Everyone'
  rights :full_control, 'DOMAIN\\User\\Files'
  action :create
end
