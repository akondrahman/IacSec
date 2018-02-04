=begin
Sample code to mess with
Puppet ASTs
Akond Rahman
Feb 03, 2018
=end

PuppetLint.new_check(:ast_example) do
   def check
      class_indexes.each do |class_ind|
         class_ind[:param_tokens].each do |para_toke|
              # value_token   = para_toke ### gives full assignment expressions: left operand, operator, right operand
              curr_token = para_toke
              prev_token = curr_token.prev_token
              next_token = curr_token.next_token
              token_val_str = curr_token.value
              token_type = curr_token.type ### gibves the type fotoken such as EQUALS , LPAREN, RPAREN
              puts "[TYPES]=> CURR: #{curr_token.type}, PREV: #{prev_token.type}, NEXT: #{next_token.type}"
              puts "[VALUE]=> CURR: #{curr_token.value}, PREV: #{prev_token.value}, NEXT: #{next_token.value}"              
         end
      end
   end
end
