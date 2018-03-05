=begin
Akond Rahman
write plugin for puppet-lint to check empty passwords
March 05, 2018
=end
PuppetLint.new_check(:no_full_binding) do
  def check
           tokens.each do |indi_token|
               nxt_token     = indi_token.next_code_token # next token which is not a white space
               if (nxt_token.nil?) || (indi_token.nil?)
                  puts ""
               else
                  token_type   = indi_token.type.to_s ### this gives type for current token

                  token_line   = indi_token.line ### this gives type for current token
                  nxt_tok_line = nxt_token.line
                  nxt_nxt_token =  nxt_token.next_code_token # get the next next token

                  if  (nxt_nxt_token.nil?)
                     puts ""
                  else
                     nxt_nxt_line = nxt_nxt_token.line
                     if (token_type.eql? 'NAME') || (token_type.eql? 'VARIABLE') || (token_type.eql? 'SSTRING')
                        puts "Token type: #{token_type}"
                        if (token_line==nxt_nxt_line)
                           token_valu  = indi_token.value.downcase
                           nxt_nxt_val = nxt_nxt_token.value.downcase
                           puts "KEY,PAIR----->#{token_valu}, #{nxt_nxt_val}"
                        end
                     end
                  end

               end
               # if token_valu.include? "0.0.0.0"
               #    notify :warning, {
               #       message: 'SECURITY:::BINDING_TO_ALL:::Do not bind to 0.0.0.0. This may cause a DDOS attack. Restrict your available IPs.',
               #       line:    indi_token.line,
               #       column:  indi_token.column,
               #       token:   token_valu
               #    }
               # end
           end
  end
end
