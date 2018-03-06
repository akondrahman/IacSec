=begin
The rules file for Chef cookbooks
Akond Rahman
Nov 25, 2017
Saturday
=end

rule "SECURITY", "Use of MD5 should be avoided" do
  tags %w{security akondrahman}
  recipe do |ast_|
     all_reso = find_resources(ast_)
     all_reso.each do |indi_reso|
         reso_dict = resource_attributes(indi_reso)
         reso_dict.each do |key_, val_|
               key2see = key_.to_s.downcase
               val2see = val_.to_s.downcase
               if (key2see.include? "md5") || (val2see.include? "md5")
                   print "SECURITY:::MD5:::Do not use MD5, as it has security weakness. Use SHA-512."
                   print "\n"
               end
         end
     end
  end
end

rule "SECURITY", "Use of BASE64 should be avoided" do
  tags %w{security akondrahman}
  recipe do |ast_|
     all_reso = find_resources(ast_)
     all_reso.each do |indi_reso|
         reso_dict = resource_attributes(indi_reso)
         reso_dict.each do |key_, val_|
               key2see = key_.to_s.downcase
               val2see = val_.to_s.downcase
               if (key2see.include? "base64") || (val2see.include? "base64")
                   print "SECURITY:::BASE64:::Do not use BASE64 for security, as it is a message encoding scheme. Use SHA-512."
                   print "\n"
               end
         end
     end
  end
end

rule "SECURITY", "Use of HTTP should be avoided" do
  tags %w{security akondrahman}
  recipe do |ast_|
     all_reso = find_resources(ast_)
     all_reso.each do |indi_reso|
         reso_dict = resource_attributes(indi_reso)
         reso_dict.each do |key_, val_|
               key2see = key_.to_s.downcase
               val2see = val_.to_s.downcase
               if (key2see.include? "http://") || (val2see.include? "http://")
                   print "SECURITY:::HTTP:::Do not use HTTP without TLS. This may cause a man in the middle attack. Use TLS with HTTP."
                   print "\n"
               end
         end
     end
  end
end

rule "SECURITY", "IP Addresses should not be bound to 0.0.0.0" do
  tags %w{security akondrahman}
  recipe do |ast_|
     all_reso = find_resources(ast_)
     all_reso.each do |indi_reso|
         reso_dict = resource_attributes(indi_reso)
         reso_dict.each do |key_, val_|
               val2see = val_.to_s.downcase
               if val2see.include? "0.0.0.0"
                   print "SECURITY:::BINDING_TO_ALL:::Do not bind to 0.0.0.0. This may cause a DDOS attack. Restrict your available IPs."
                   print "\n"
               end
         end
     end
  end
end

rule "SECURITY", "SSH keys hould not be hard-coded" do
  tags %w{security akondrahman}
  recipe do |ast_|
     find_resources(ast_, :type => 'execute').select do |exec_reso|
        #print "#{exec_reso}"
        cmd_str = resource_attribute(exec_reso, 'command').to_s
        #print "#{cmd_str}"
        cmd_str.match(/ssh-rsa\s(\w)*/) ? true : false ## for ruby regex see http://rubular.com/
     end
  end
end

rule "SECURITY", "Use of empty password should be avoided" do
  tags %w{security akondrahman}
  recipe do |ast_|
     all_reso = find_resources(ast_)
     all_reso.each do |indi_reso|
         reso_dict = resource_attributes(indi_reso)
         reso_dict.each do |key_, val_|
               key2see = key_.to_s.downcase
               if ((key2see.include? "pwd") || (key2see.include? "password") || (key2see.include? "pass")) && ((val_.length <=0) || (val_.eql? ' '))
                   print "SECURITY:::EMPTY_PASSWORD:::Do not keep password field empty. This may help an attacker to attack. You can use hiera to avoid this issue."
                   print "\n"
               end
         end
     end
  end
end

# rule "MYRULE002", "Drive letter should not be in path" do
#   tags %w{security akondrahman}
#   recipe do |ast_, filename_|
#       matchCnt = 0
#       lines  = []
#       ###read cookbook line by line to see if drive letter appears
#       text_content=File.open(filename_).read
#       text_content.gsub!(/\r\n?/, "\n")
#       text_content.each_line do |line_as_str|
#          line_as_str = line_as_str.downcase
#          if line_as_str.include?('c:')
#             #matchCnt += 1
#             print "MYRULE002: Drive letter should not be in path"
#             print "\n"
#          end
#       end
#   end
# end



rule "SECURITY", "SUSPICOUS_COMMENTS" do
  tags %w{security akondrahman}
  kw_list = ['show_bug', 'hack', 'fixme', 'later', 'later2', 'todo', 'ticket', 'launchpad']
  recipe do |ast_, filename_|
      matchCnt = 0
      lines  = []
      text_content=File.open(filename_).read
      text_content.gsub!(/\r\n?/, "\n")
      text_content.each_line do |line_as_str|
         if line_as_str.include?('#')
            # print 'Asi mama'
            comment_index = line_as_str.index('#')
            single_line = line_as_str.downcase
            kw_list.each do |kw_|
               if (single_line.include?(kw_))
                  kw_index = single_line.index(kw_)
                     if (kw_index > comment_index)
                        print "SECURITY:::SUSPICOUS_COMMENTS:::Bug information exposed in comments."
                        print "\n"
                     end
               end
            end
         end
      end
  end
end





rule "SECURITY", "Use of hard-coded secrets should be avoided" do
  tags %w{security akondrahman}
  recipe do |ast_|
     all_reso = find_resources(ast_)
     all_reso.each do |indi_reso|
         reso_dict = resource_attributes(indi_reso)
         reso_dict.each do |key_, val_|
               key2see = key_.to_s.downcase
               val2see = val_.to_s.downcase
               if (((key2see.include? 'pwd') || (key2see.include? 'password') || (key2see.include? 'pass') ||
                    (key2see.include? 'uuid') || (key2see.include? 'key') || (key2see.include? 'crypt') ||
                    (key2see.include? 'secret') || (key2see.include? 'certificate') || (key2see.include? 'id') ||
                    (key2see.include? 'cert') || (key2see.include? 'token') || (key2see.include? 'ssh_key') ||
                    (key2see.include? 'md5') || (key2see.include? 'rsa') || (key2see.include? 'ssl')) && (val2see.length > 0))
                      print "SECURITY:::HARD_CODED_SECRET_V1:::Do not hard code secrets. This may help an attacker to attack the system. You can use 'data bags' to avoid this issue."
                      print "\n"
               end
         end
     end
  end
end
