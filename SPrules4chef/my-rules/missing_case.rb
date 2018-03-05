=begin
Akond Rahman
Extra Khatir for Missing Default Handling
Feb 12, 2018
=end
require 'rubocop'  ### need to import module 'RubCop' for detecting missing default case

dir_to_mine = '/Users/akond/SECU_REPOS/test-chef/'
Dir.chdir(dir_to_mine)
all_files = Dir.glob("**/*.rb")

all_files.each do |file_|
  if (File.extname(file_).eql? '.rb') && (file_.include? 'recipes') && (!file_.include? 'acceptance')
     puts "Mining:#{file_}"
     # filename_ = '/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/IacSec/SPrules4chef/create_win_dir.rb'
     code_content = File.read(file_)
     # print code_content
     # print " "

     source = RuboCop::ProcessedSource.new(code_content, RUBY_VERSION.to_f)
     node = source.ast
     begin
         cand_child_nodes = node.child_nodes()
     rescue NoMethodError => err_str
           print_exception(err_str, true)
     end
     cand_child_nodes.each do |child_node|
          if child_node.case_type?
             # puts child_node.when_branches()
             else_content =child_node.else_branch.to_s()
             else_len = else_content.length
             if (else_len <= 0)
                print "SECURITY:::MISSING_DEFAULT:::Default case (else block) is missing."
                print "\n"
             end
          end
     end
  end
end
