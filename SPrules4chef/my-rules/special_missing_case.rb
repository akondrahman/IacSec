=begin
Missing default case : special rule handling 
Akond Rahman
Nov 22, 2018
Thrusday 
=end

require 'rubocop'  ### need to import module 'RuboCop' for detecting missing default case

filename_ = ARGV[0] 
filename_ = filename_.chomp 
code_content = File.read(filename_)

source = RuboCop::ProcessedSource.new(code_content, RUBY_VERSION.to_f)
node = source.ast
begin
    cand_child_nodes = node.child_nodes()
rescue NoMethodError => err_str
    print_exception(err_str, true)
end
cand_child_nodes.each do |child_node|
    if child_node.case_type?
        else_content =child_node.else_branch.to_s()
        else_len = else_content.length
        if (else_len <= 0)
           print "SECURITY:::MISSING_DEFAULT:::Default case (else block) is missing. Need to add a default case"
           print "\n"
        end
    end
end
