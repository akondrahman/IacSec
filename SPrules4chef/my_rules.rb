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
        #print "#{cmd_str}"
        cmd_str.match(/ssh-rsa\s(\w)*/) ? true : false ## for ruby regex see http://rubular.com/
     end
  end
end


rule "MYRULE002", "Drive letter should not be in path" do
  tags %w{security akondrahman}
  matchCnt = 0
  recipe do |ast_, filename_|
      #puts filename_.inspect
      ###read cookbook line by line to see if drive letter appears
      text_content=File.open(filename_).read
      text_content.gsub!(/\r\n?/, "\n")
      text_content.each_line do |line_as_str|
         line_as_str = line_as_str.downcase
         if(line_as_str.include?('c:'))
           matchCnt += 1
         end
      end
  end
  matchCnt 
end
