=begin
Akond Rahman
write plugin for puppet-lint to check use of BASE 64
March 11, 2018
=end
PuppetLint.new_check(:no_base64) do

  def check
           tokens.each do |indi_token|
               token_valu = indi_token.value ### this gives each token
               token_valu = token_valu.downcase
               token_type = indi_token.type.to_s
               if (token_valu.include? "base64") && (!token_type.eql? "COMMENT")
                  notify :warning, {
                     message: 'SECURITY:::BASE64:::Do not use BASE64 for security, as it is a message encoding scheme. Use SHA-512.@'+token_valu+'@',
                     line:    indi_token.line,
                     column:  indi_token.column,
                     token:   token_valu
                  }
               end
           end
  end

end

PuppetLint.new_check(:no_admin_by_default) do
  def check
           tokens.each do |indi_token|
               nxt_token     = indi_token.next_code_token # next token which is not a white space
               if (!nxt_token.nil?) && (!indi_token.nil?)
                  token_type   = indi_token.type.to_s ### this gives type for current token

                  nxt_nxt_token =  nxt_token.next_code_token # get the next next token to get key value pair

                  if  (!nxt_nxt_token.nil?)
                     token_line      = indi_token.line ### this gives type for current token
                     nxt_tok_line    = nxt_token.line
                     nxt_nxt_tok_lin = nxt_nxt_token.line
                     if (token_type.eql? 'NAME') || (token_type.eql? 'VARIABLE') || (token_type.eql? 'SSTRING')
                        nxt_typ = nxt_token.type.to_s
                        nxt_nxt_typ=nxt_nxt_token.type.to_s
                        if (token_line==nxt_tok_line) && (token_line==nxt_nxt_tok_lin)
                           if (token_type.eql? 'VARIABLE') && (nxt_typ.eql? 'EQUALS') && (nxt_nxt_typ.eql? 'SSTRING')
                                # puts "ONE,TWO,THREE----->#{token_type}, #{nxt_typ}, #{nxt_nxt_typ}"
                                nxt_nxt_val = nxt_nxt_token.value.downcase
                                token_val   = indi_token.value.downcase
                                if ((nxt_nxt_val.include? 'admin') && (token_val.include? 'user')) ||
                                   ((token_val.include? 'admin') && (token_val.include? 'user'))
                                   notify :warning, {
                                     message: 'SECURITY:::ADMIN_BY_DEFAULT:::Do not make default user as admin. This violates the secure by design principle.@'+token_val+'='+nxt_nxt_val+'@',
                                     line:    indi_token.line,
                                     column:  indi_token.column,
                                     token:   token_val
                                   }
                                end
                           end
                        end
                     end
                  end
               end
           end
  end
end

PuppetLint.new_check(:no_empty_pass) do
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
                           if (((token_valu.include? "pwd") || (token_valu.include? "password") || (token_valu.include? "pass")) && ((nxt_nxt_val.length <=0) || (nxt_nxt_val.eql?' ')))
                              notify :warning, {
                                message: 'SECURITY:::EMPTY_PASSWORD:::Do not keep password field empty. This may help an attacker to attack. You can use hiera to avoid this issue.@'+token_valu+'='+nxt_nxt_val+'@',
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
PuppetLint.new_check(:no_full_binding) do
  def check
           tokens.each do |indi_token|
               token_valu = indi_token.value ### this gives each token
               token_valu = token_valu.downcase
               token_type = indi_token.type.to_s
               if (token_valu.include? "0.0.0.0") && (!token_type.eql? "COMMENT")
                  notify :warning, {
                     message: 'SECURITY:::BINDING_TO_ALL:::Do not bind to 0.0.0.0. This may cause a DDOS attack. Restrict your available IPs.@'+token_valu+'@',
                     line:    indi_token.line,
                     column:  indi_token.column,
                     token:   token_valu
                  }
               end
           end
  end
end



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
                                (token_valu.include? "md5") || (token_valu.include? "rsa") || (token_valu.include? "ssl")
                               ) && ((nxt_nxt_val.length > 0)) && ((!nxt_nxt_type.eql? 'VARIABLE')) &&
                               ((!nxt_nxt_val.include? "(") && (!nxt_nxt_val.include? 'undef') && (!nxt_nxt_val.include? 'true') && (!nxt_nxt_val.include? 'false') &&
                                (!nxt_nxt_val.include? 'hiera') && (!nxt_nxt_val.include? 'secret') && (!nxt_nxt_val.include? 'union') && (!nxt_nxt_val.include? '${') &&
                                (!nxt_nxt_val.include? '$')
                               )
                              )
                                 # && (nxt_nxt_val.is_a? String)
                                 # puts "KEY,PAIR,CURR_TYPE,NEXT_TYPE----->#{token_valu}, #{nxt_nxt_val}, #{token_type}, #{nxt_nxt_type}"
                                 notify :warning, {
                                    message: 'SECURITY:::HARD_CODED_SECRET_V1:::Do not hard code secrets. This may help an attacker to attack the system. You can use hiera to avoid this issue.@'+token_valu+'='+nxt_nxt_val+'@',
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


PuppetLint.new_check(:no_hardcode_secret_v2) do
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

                           if ((nxt_nxt_val.length > 0) && (!nxt_nxt_type.eql? 'VARIABLE') && (nxt_nxt_val.include? 'ssh-rsa'))
                                 notify :warning, {
                                    message: 'SECURITY:::HARD_CODED_SECRET_V2:::Do not hard code secrets. This may help an attacker to attack the system. You can use hiera to avoid this issue.@'+token_valu+'='+nxt_nxt_val+'@',
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
PuppetLint.new_check(:no_http) do
  def check
           tokens.each do |indi_token|
               token_valu = indi_token.value ### this gives each token
               token_valu = token_valu.downcase
               token_type = indi_token.type.to_s
               if (token_valu.include? "http://" ) && (!token_type.eql? "COMMENT")
                  notify :warning, {
                     message: 'SECURITY:::HTTP:::Do not use HTTP without TLS. This may cause a man in the middle attack. Use TLS with HTTP.@'+token_valu+'@',
                     line:    indi_token.line,
                     column:  indi_token.column,
                     token:   token_valu
                  }
               end
           end
  end
end



PuppetLint.new_check(:no_md5) do

  def check
           tokens.each do |indi_token|
               token_valu = indi_token.value ### this gives each token
               token_valu = token_valu.downcase
               # print "#{token_name} \t"
               token_type = indi_token.type.to_s
               if (token_valu.include? "md5") && (!token_type.eql? "COMMENT")
                  notify :warning, {
                     message: 'SECURITY:::MD5:::Do not use MD5, as it has security weakness. Use SHA-512.@' + token_valu+'@',
                     line:    indi_token.line,
                     column:  indi_token.column,
                     token:   token_valu
                  }
               end
           end
  end

end
PuppetLint.new_check(:no_expose_secret_location) do
  def check
           tokens.each do |indi_token|
               nxt_token     = indi_token.next_code_token # next token which is not a white space
               if (!nxt_token.nil?) && (!indi_token.nil?)
                  token_type   = indi_token.type.to_s ### this gives type for current token

                  token_line   = indi_token.line ### this gives line for current token
                  nxt_tok_line = nxt_token.line

                  nxt_nxt_token =  nxt_token.next_code_token # get the next next token to get key value pair

                  if  (!nxt_nxt_token.nil?)
                     nxt_nxt_line = nxt_nxt_token.line
                     if (token_type.eql? 'NAME') || (token_type.eql? 'VARIABLE') || (token_type.eql? 'SSTRING')
                        if (token_line==nxt_nxt_line)
                           token_val   = indi_token.value.downcase ### this gives value for current token

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
                                message: 'SECURITY:::EXPOSING_SECRET_LOCATION:::Do not expose location of secrets. This may help an attacker to attack. You can use hiera to avoid this issue.@' + token_val +'='+nxt_nxt_val+'@',
                                line:    nxt_nxt_token.line,
                                column:  nxt_nxt_token.column,
                                token:   token_val
                              }
                           end
                        end
                     end
                  end
               end
           end
  end
end

PuppetLint.new_check(:no_susp_comments) do

  def check
     ##for comments we need to grab all lines
     lineNo=0
     manifest_lines.each do |single_line|
        lineNo += 1
        ##first check if string starts with #, which is comemnt in Puppet
        if single_line.include? '#'
           ### check if those keywords exist
           single_line=single_line.downcase
           single_line=single_line.strip
           # (single_line.include?('show_bug') || removing show_bug, as it generates duplicates
           if  (( single_line.include?('hack') ||
                single_line.include?('fixme')    || single_line.include?('later') ||
                single_line.include?('later2')   || single_line.include?('todo') ||
                single_line.include?('ticket')   || single_line.include?('launchpad') ||
                single_line.include?('bug') ) && (!single_line.include?('debug'))
               )
                #print "#{single_line} #{lineNo}\n"
                #print "-----\n"
                notify :warning, {
                  message: 'SECURITY:::SUSPICOUS_COMMENTS:::Do not expose sensitive information@' + single_line+'@',
                  line:    lineNo,
                  column:   5   #no columsn for comment lines so assignning a dummy one to keep puppet-lint happy
                }
           end
        end
     end
  end
end
