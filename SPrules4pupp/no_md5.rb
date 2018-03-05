=begin
Akond Rahman
write plugin for puppet-lint to check use of MD5
March 05, 2018
=end
PuppetLint.new_check(:no_md5) do

  def check
           tokens.each do |indi_token|
               token_valu = indi_token.value ### this gives each token
               token_valu = token_valu.downcase
               # print "#{token_name} \t"
               if token_valu.include? "md5"
                  notify :warning, {
                     message: 'SECURITY:::MD5:::Do not use MD5, as it has security weakness. Use SHA-512',
                     line:    indi_token.line,
                     column:  indi_token.column,
                     token:   token_valu
                  }
               end
           end
  end

end




=begin
resource_indexes.each do |resource|
  resource[:param_tokens].each do |param_token|   ## if you use resource , then you will get resources, but not all

                 # token_val  = param_token.value
                 # print "#{token_val} \t"
=end
