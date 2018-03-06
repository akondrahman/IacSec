=begin
Akond Rahman
write plugin for puppet-lint to check exposure of secret key locations
March 06, 2018
=end
PuppetLint.new_check(:no_expose_secret_location) do
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
                        if (token_line==nxt_nxt_line)
                           nxt_nxt_val = nxt_nxt_token.value.downcase
                           nxt_nxt_typ = nxt_nxt_token.type.to_s
                           # puts "PAIR,PAIR_TYPE----->#{nxt_nxt_val}, #{nxt_nxt_typ}"
                           if ( ((nxt_nxt_val.include? "rsa")  || (nxt_nxt_val.include? "ssh") ||
                                (nxt_nxt_val.include? "pem") || (nxt_nxt_val.include? "crt") ||
                                (nxt_nxt_val.include? "key") || (nxt_nxt_val.include? "ssl") ||
                                (nxt_nxt_val.include? "certificate") || (nxt_nxt_val.include? "crl") ||
                                (nxt_nxt_val.include? "pub") || (nxt_nxt_val.include? "id")) &&
                                ((nxt_nxt_val.start_with? '/') || (nxt_nxt_val.include? '\\')) && 
                                (nxt_nxt_typ.eql? 'SSTRING')
                              )
                              notify :warning, {
                                message: 'SECURITY:::EXPOSING_SECRET_LOCATION:::Do not expose location of secrets. This may help an attacker to attack. You can use hiera to avoid this issue.',
                                line:    nxt_nxt_token.line,
                                column:  nxt_nxt_token.column,
                                token:   nxt_nxt_val
                              }
                           end
                        end
                     end
                  end
               end
           end
  end
end
