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
  kw_list = ['bug', 'hack', 'fixme', 'later', 'later2', 'todo']
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
