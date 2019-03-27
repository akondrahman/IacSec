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

rule "SECURITY", "Use of HTTP should be avoided (V1)" do
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

rule "SECURITY", "Use of HTTP should be avoided (V2)" do
   tags %w{security akondrahman}
   recipe do |ast_, filename_|
      text_content=File.open(filename_).read
      text_content.gsub!(/\r\n?/, "\n")
      text_content.each_line do |line_as_str|
         if (! line_as_str.include?('#')) && ( line_as_str.include?('=>')) 
               single_line = line_as_str.downcase
               if (single_line.include?("http://"))  
                  print "SECURITY:::HTTP:::Do not use HTTP without TLS. This may cause a man in the middle attack. Use TLS with HTTP."
                  print "\n"
               end
         end    
      end
   end
 end

# rule "SECURITY", "IP Addresses should not be bound to 0.0.0.0 (V1)" do
#   tags %w{security akondrahman}
#   recipe do |ast_|
#      all_reso = find_resources(ast_)
#      all_reso.each do |indi_reso|
#          reso_dict = resource_attributes(indi_reso)
#          reso_dict.each do |key_, val_|
#                val2see = val_.to_s.downcase
#                if val2see.include? "0.0.0.0"
#                    print "SECURITY:::BINDING_TO_ALL:::Do not bind to 0.0.0.0. This may cause a DDOS attack. Restrict your available IPs."
#                    print "\n"
#                end
#          end
#      end
#   end
# end

# rule "SECURITY", "SSH keys hould not be hard-coded" do
#   tags %w{security akondrahman}
#   recipe do |ast_|
#      find_resources(ast_, :type => 'execute').select do |exec_reso|
#         #print "#{exec_reso}"
#         cmd_str = resource_attribute(exec_reso, 'command').to_s
#         #print "#{cmd_str}"
#         cmd_str.match(/ssh-rsa\s(\w)*/) ? true : false ## for ruby regex see http://rubular.com/
#      end
#   end
# end

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
  kw_list = ['show_bug', 'hack', 'fixme', 'later', 'later2', 'todo', 'ticket', 'launchpad', 'bug']
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
                        print "SECURITY:::SUSPICOUS_COMMENTS:::Do not expose sensitive information=>"
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
                      print "SECURITY:::HARD_CODED_SECRET_:::Do not hard code secrets. This may help an attacker to attack the system. You can use 'data bags' to avoid this issue."
                      print "\n"
               end
         end
     end
  end
end




# rule "SECURITY", "Locations of secrets should not be exposed (V1)" do
#   tags %w{security akondrahman}
#   recipe do |ast_|
#      all_reso = find_resources(ast_)
#      all_reso.each do |indi_reso|
#          reso_dict = resource_attributes(indi_reso)
#          reso_dict.each do |key_, val_|
#                key2see = key_.to_s.downcase
#                val2see = val_.to_s.downcase
#                if (((val2see.include? 'rsa') || (val2see.include? 'ssh') || (val2see.include? 'pem') ||
#                     (val2see.include? 'crt') || (val2see.include? 'key') || (val2see.include? 'ssl') ||
#                     (val2see.include? 'certificate') || (val2see.include? 'crl') || (val2see.include? 'pub') ||
#                     (val2see.include? 'id')) && ((val2see.start_with? '/') || ((val2see.include? '\\') && (val2see.include? ':')))
#                   )
#                       # puts "VALUE: #{val2see}"
#                       print "SECURITY:::EXPOSING_SECRET_LOCATION_V1:::Do not expose location of secrets. This may help an attacker to attack. You can use 'data bags' to avoid this issue."
#                       print "\n"
#                end
#          end
#      end
#   end
# end


# reff: https://www.reddit.com/r/aws/comments/5nx418/what_does_00000_means/
rule "SECURITY", "IP Addresses should not be bound to 0.0.0.0 (V2)" do
  tags %w{security akondrahman}
  recipe do |ast_, filename_|
      text_content=File.open(filename_).read
      text_content.gsub!(/\r\n?/, "\n")
      text_content.each_line do |line_as_str|
            single_line = line_as_str.downcase
            if ((single_line.include? '0.0.0.0') && (! line_as_str.include?('#'))) 
                   # puts single_line
                   print "SECURITY:::BINDING_TO_ALL:::Do not bind to 0.0.0.0. This may cause a DDOS attack. Restrict your available IPs."
                   print "\n"
            end
      end
  end
end
rule "SECURITY", "Locations of secrets should not be exposed (V2)" do
  tags %w{security akondrahman}
  recipe do |ast_, filename_|
      text_content=File.open(filename_).read
      text_content.gsub!(/\r\n?/, "\n")
      text_content.each_line do |line_as_str|
               single_line = line_as_str.downcase
               if (((single_line.include? 'rsa') || (single_line.include? 'ssh') || (single_line.include? 'pem') ||
                    (single_line.include? 'crt') || (single_line.include? 'key') || (single_line.include? 'ssl') ||
                    (single_line.include? 'certificate') || (single_line.include? 'crl') || (single_line.include? 'pub') ||
                    (single_line.include? 'id')) && ((single_line.include? '/') || ((single_line.include? '\\') && (single_line.include? ':')))
                  )
                      # puts "VALUE: #{single_line}"
                      print "SECURITY:::EXPOSING_SECRET_LOCATION_V2:::Do not expose location of secrets. This may help an attacker to attack. You can use 'data bags' to avoid this issue."
                      print "\n"
               end
      end
  end
end

# integrity check rule for nodes 
rule "INTEGRITY_CHECK_1", "NO_CHECKSUM" do
  tags %w{security akondrahman}
  prop_list = []
  recipe do |ast|
    noed_array = attribute_access(ast, :type => :string).find_all do |tmp_| 
      tmp_.each do |key_, val_|
         key2see = key_.to_s.downcase
         val2see = val_.to_s.downcase
         prop_list.push(val2see)
      end
    end 
    if  ( (!(prop_list.include? 'checksum') || !(prop_list.include? 'checksum_linux_x64') || !(prop_list.include? 'checksum_linux_x86') || !(prop_list.include? 'check_sha') || !(prop_list.include? 'gcc_installer_checksum')) && 
        ((prop_list.include? 'src_url') || (prop_list.include? 'repo_rpm_url') || (prop_list.include? 'gcc_installer_url') || (prop_list.include? 'url')) 
        )
            print 'SECURITY:::SOURCE_INTEGRITY:::ATTRIBUTE:::Validate downloaded content using checksum' 
            print '\n'
    end
  end
end

#reff: https://gist.github.com/maplebed/24ebfdc4f0d0c0cd0cfd3667228cd0bf
rule "INTEGRITY_CHECK_2", "NO_CHECKSUM" do
  tags %w{security akondrahman}
  repo_flag  = false 
  check_flag = false 
  list_flag  = []
  recipe do |ast_, filename_|
      text_content=File.open(filename_).read
      text_content.gsub!(/\r\n?/, "\n")
      text_content.each_line do |line_as_str|
            single_line = line_as_str.downcase
            if ( (single_line.include? '.tgz') || (single_line.include? '.tar.gz') || (single_line.include? 'repo_url') ||  (single_line.include? '.rpm') || (single_line.include? 'package_url') || (single_line.include? '.dmg')  )  && (single_line.include? 'http') 
              repo_flag = true 
            end 
            if (( (single_line.include? 'checksum') || (single_line.include? 'gpgcheck') || (single_line.include? 'checksha') ) && (! single_line.include? 'false') )
              check_flag = true 
            end
            temp_list = []
            temp_list.push(repo_flag) 
            temp_list.push(check_flag)  
            list_flag.push(temp_list)
            # puts "VALUE: #{list_flag}"
      end
      list_flag.each do |sub_lis|
            if (sub_lis.length > 0)
                  repo_flag_  = sub_lis[0]
                  check_flag_ = sub_lis[1]
                  if (repo_flag_) && (!check_flag_)
                     print 'SECURITY:::SOURCE_INTEGRITY:::LINES:::Validate downloaded content using checksum' 
                     print '\n'     
                  end
            end 
      end 
      list_flag  = []
  end 
end

rule "SECURITY", "Use of hard-coded secrets (password) to be avoided" do
  tags %w{security akondrahman}
  kw_list = ['password', 'pass'] 
  recipe do |ast_, filename_|
      matchCnt = 0
      lines  = []
      text_content=File.open(filename_).read
      text_content.gsub!(/\r\n?/, "\n")
      text_content.each_line do |line_as_str|
         if (! line_as_str.include?('#')) && (! line_as_str.include?('(')) 
            single_line = line_as_str.downcase
            kw_list.each do |kw_|
              if (single_line.include?(kw_)) && ( (single_line.include?(':'))  || (single_line.include?('=')) )
                  print "SECURITY:::HARD_CODED_SECRET_:::Do not hard code secrets. This may help an attacker to attack the system. You can use 'data bags' to avoid this issue."
                  print "\n"
               end
            end
         end
      end
  end
end

rule "SECURITY", "Use of hard-coded passwords to be avoided" do
  tags %w{security akondrahman}
  kw_list = ['password', 'pass']
  recipe do |ast_, filename_|
      matchCnt = 0
      lines  = []
      text_content=File.open(filename_).read
      text_content.gsub!(/\r\n?/, "\n")
      text_content.each_line do |line_as_str|
         if (! line_as_str.include?('#')) && (! line_as_str.include?('(')) 
            single_line = line_as_str.downcase
            kw_list.each do |kw_|
               if (single_line.include?(kw_)) && ( (single_line.include?(':'))  || (single_line.include?('=')) )
                  print "SECURITY:::HARD_CODED_SECRET_PASSWORD:::Do not hard code passwords. This may help an attacker to attack the system. You can use 'data bags' to avoid this issue."
                  print "\n"
               end
            end
         end
      end
  end
end

rule "SECURITY", "Use of hard-coded secrets (username) to be avoided" do
  tags %w{security akondrahman}
  kw_list = ['username'] 
  recipe do |ast_, filename_|
      matchCnt = 0
      lines  = []
      text_content=File.open(filename_).read
      text_content.gsub!(/\r\n?/, "\n")
      text_content.each_line do |line_as_str|
         if (! line_as_str.include?('#')) && (! line_as_str.include?('(')) 
            single_line = line_as_str.downcase
            kw_list.each do |kw_|
              if (single_line.include?(kw_)) && ( (single_line.include?(':'))  || (single_line.include?('=')) )
                  print "SECURITY:::HARD_CODED_SECRET_:::Do not hard code secrets. This may help an attacker to attack the system. You can use 'data bags' to avoid this issue."
                  print "\n"
               end
            end
         end
      end
  end
end


rule "SECURITY", "Use of hard-coded usernames  to be avoided" do
  tags %w{security akondrahman}
  kw_list = ['username']
  recipe do |ast_, filename_|
      matchCnt = 0
      lines  = []
      text_content=File.open(filename_).read
      text_content.gsub!(/\r\n?/, "\n")
      text_content.each_line do |line_as_str|
         if (! line_as_str.include?('#')) && (! line_as_str.include?('(')) 
            single_line = line_as_str.downcase
            kw_list.each do |kw_|
               if (single_line.include?(kw_)) && ( (single_line.include?(':'))  || (single_line.include?('=')) )
                  print "SECURITY:::HARD_CODED_SECRET_USER_NAME:::Do not hard code usernames. This may help an attacker to attack the system. You can use 'data bags' to avoid this issue."
                  print "\n"
               end
            end
         end
      end
  end
end

rule "SECURITY", "Do not use weak crypotgraphy algorithms such as MD5" do
   tags %w{security akondrahman}
   kw_list = ['md5']
   recipe do |ast_, filename_|
       matchCnt = 0
       lines  = []
       text_content=File.open(filename_).read
       text_content.gsub!(/\r\n?/, "\n")
       text_content.each_line do |line_as_str|
          if (! line_as_str.include?('#')) 
             single_line = line_as_str.downcase
             kw_list.each do |kw_|
                if (single_line.include?(kw_)) &&  (single_line.include?('=>'))  
                   print "SECURITY:::MD5:::Do not use MD5, as it has security weakness. Use SHA-512."
                   print "\n"
                end
             end
          end
       end
   end
 end

 rule "SECURITY", "Use of admin as default users should be avoided" do
   tags %w{security akondrahman}
   kw_list = ['admin']
   recipe do |ast_, filename_|
       text_content=File.open(filename_).read
       text_content.gsub!(/\r\n?/, "\n")
       text_content.each_line do |line_as_str|
          if (! line_as_str.include?('#')) && (! line_as_str.include?('=>')) 
             single_line = line_as_str.downcase
             kw_list.each do |kw_|
                if (single_line.include?(kw_)) 
                   print "SECURITY:::ADMIN_BY_DEFAULT:::Do not make default user as admin. This violates the secure by design principle."
                   print "\n"
                end
             end
          end
       end
   end
 end

##command foodcritic -I SPrules4chef/my-rules/my_rules.rb SPrules4chef/create_win_dir.rb 