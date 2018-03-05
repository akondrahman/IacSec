=begin
Akond Rahman
write plugin for puppet-lint to check use of BASE 64
March 05, 2018
=end
PuppetLint.new_check(:no_base64) do

  def check
           tokens.each do |indi_token|
               token_valu = indi_token.value ### this gives each token
               token_valu = token_valu.downcase
               if token_valu.include? "base64"
                  notify :warning, {
                     message: 'SECURITY:::BASE64:::Do not use BASE64 for security, as it is a message encoding scheme. Use SHA-512.',
                     line:    indi_token.line,
                     column:  indi_token.column,
                     token:   token_valu
                  }
               end
           end
  end

end
