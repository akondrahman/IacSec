=begin
Akond Rahman
write plugin for puppet-lint to check hard-coded secrets
March 05, 2018
=end
PuppetLint.new_check(:no_hardcode_secret_v1) do
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
                     if (token_type.eql? 'NAME') || (token_type.eql? 'VARIABLE')
                        # puts "Token type: #{token_type}"
                        if (token_line==nxt_nxt_line)
                           token_valu   = indi_token.value.downcase
                           nxt_nxt_val  = nxt_nxt_token.value.downcase
                           nxt_nxt_type = nxt_nxt_token.type.to_s  ## to handle false positives,

                           if (((token_valu.include? "pwd") || (token_valu.include? "password") || (token_valu.include? "pass") ||
                                (token_valu.include? "uuid") || (token_valu.include? "key") || (token_valu.include? "crypt") ||
                                (token_valu.include? "secret") || (token_valu.include? "certificate") || (token_valu.include? "id") ||
                                (token_valu.include? "cert") || (token_valu.include? "token") || (token_valu.include? "ssh_key") ||
                                (token_valu.include? "md5") && (!token_valu.include? "{")
                               ) && ((nxt_nxt_val.length > 0)) && ((!nxt_nxt_type.eql? 'VARIABLE')))
                                 # puts "KEY,PAIR,CURR_TYPE,NEXT_TYPE----->#{token_valu}, #{nxt_nxt_val}, #{token_type}, #{nxt_nxt_type}"
                                 notify :warning, {
                                    message: 'SECURITY:::HARD_CODED_SECRET:::Do not hard code secrets. This may help an attacker to attack the system. You can use hiera to avoid this issue.',
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
