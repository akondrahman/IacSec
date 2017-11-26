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
  recipe do |ast_, filename_|
      matchCnt = 0
      lines  = []
      ###read cookbook line by line to see if drive letter appears
      text_content=File.open(filename_).read
      text_content.gsub!(/\r\n?/, "\n")
      text_content.each_line do |line_as_str|
         line_as_str = line_as_str.downcase
         if line_as_str.include?('c:')
            #matchCnt += 1
            print "MYRULE002: Drive letter should not be in path \n"
         end
      end
  end
end



rule "MYRULE003", "Suspicious comments" do
  tags %w{security akondrahman}
  recipe do |ast_, filename_|
      matchCnt = 0
      lines  = []
      text_content=File.open(filename_).read
      text_content.gsub!(/\r\n?/, "\n")
      text_content.each_line do |line_as_str|
         if line_as_str.include?('#')
            single_line = line_as_str.downcase
            if (single_line.include?('bug') || single_line.include?('hack') || single_line.include?('fixme') || single_line.include?('later') || single_line.include?('later2') || single_line.include?('todo'))
               print "MYRULE003: Suspicious comment \n"
            end
         end
      end
  end
end
