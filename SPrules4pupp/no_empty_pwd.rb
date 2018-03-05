=begin
Akond Rahman
write plugin for puppet-lint to check empty passwords
March 05, 2018
=end
PuppetLint.new_check(:no_full_binding) do
  def check
           tokens.each do |indi_token|
               nxt_token     = indi_token.next_code_token # next token which is not a white space
               if (!nxt_token.nil?) && (!indi_token.nil?)
                  token_type   = indi_token.type.to_s ### this gives type for current token

                  token_line   = indi_token.line ### this gives type for current token
                  nxt_tok_line = nxt_token.line

                  nxt_nxt_token =  nxt_token.next_code_token # get the next next token to get key value pair

                  if  (!nxt_nxt_token.nil?)
                     nxt_nxt_line = nxt_nxt_token.line
                     if (token_type.eql? 'NAME') || (token_type.eql? 'VARIABLE') || (token_type.eql? 'SSTRING')
                        # puts "Token type: #{token_type}"
                        if (token_line==nxt_nxt_line)
                           token_valu  = indi_token.value.downcase
                           nxt_nxt_val = nxt_nxt_token.value.downcase
                           # puts "KEY,PAIR----->#{token_valu}, #{nxt_nxt_val}"
                           if(token_valu.include? "pwd") || (token_valu.include? "password") || (token_valu.include? "pass") && (nxt_nxt_val.length <=0)
                              notify :warning, {
                                message: 'SECURITY:::EMPTY_PASSWORD:::Do not keep password field empty. This may help an attacker to attack. Use hiera to import value.',
                                line:    indi_token.line,
                                column:  indi_token.column,
                                token:   token_valu
                              }
                           end
                        end
                     end
                  end
               end
           end
  end
end
