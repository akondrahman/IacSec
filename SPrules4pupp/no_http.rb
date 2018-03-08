=begin
Akond Rahman
write plugin for puppet-lint to check use of HTTP
March 05, 2018
=end
PuppetLint.new_check(:no_http) do
  def check
           tokens.each do |indi_token|
               token_valu = indi_token.value ### this gives each token
               token_valu = token_valu.downcase
               token_type = indi_token.type.to_s
               if (token_valu.include? "http://" ) && (!token_type.eql? "COMMENT")
                  notify :warning, {
                     message: 'SECURITY:::HTTP:::Do not use HTTP without TLS. This may cause a man in the middle attack. Use TLS with HTTP.',
                     line:    indi_token.line,
                     column:  indi_token.column,
                     token:   token_valu
                  }
               end
           end
  end
end
