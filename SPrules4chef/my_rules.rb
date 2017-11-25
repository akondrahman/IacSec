=begin
The rules file for Chef cookbooks
Akond Rahman
Nov 25, 2017
Saturday
=end
rule "MYRULE001", "SSH keys hould not be hard-coded" do
  tags %w{security akondrahman}
  recipe do |ast_|
     find_resources(ast_, :type => 'execute').select do |exec_reso|
        #print "#{exec_reso}"
        cmd_str = resource_attribute(exec_reso, 'command').to_s
        print "#{cmd_str}"
     end
  end
end
