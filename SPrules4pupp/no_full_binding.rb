=begin
Akond Rahman
write plugin for puppet-lint to check binding to 0.0.0.0
March 05, 2018
=end
PuppetLint.new_check(:no_full_binding) do
  def check
           tokens.each do |indi_token|
               token_valu = indi_token.value ### this gives each token
               token_valu = token_valu.downcase
               token_type = indi_token.type.to_s
               if (token_valu.include? "0.0.0.0") && (!token_type.eql? "COMMENT")
                  notify :warning, {
                     message: 'SECURITY:::BINDING_TO_ALL:::Do not bind to 0.0.0.0. This may cause a DDOS attack. Restrict your available IPs.',
                     line:    indi_token.line,
                     column:  indi_token.column,
                     token:   token_valu
                  }
               end
           end
  end
end
