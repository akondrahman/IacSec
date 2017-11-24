=begin
Akond Rahman
First attempt
write plugin for puppet-lint to check hardcoded ssh keys
Nov 24, 2017
=end
PuppetLint.new_check(:no_hardcode_key) do

  def check
       resource_indexes.each do |resource|
           resource[:param_tokens].each do |param_token|
               value_token   = param_token.next_code_token.next_code_token
               token_val_str = value_token.value
               #print "#{value_token.value}"
               if token_val_str.include? "ssh-rsa"
                  notify :warning, {
                     message: 'Do not use hard-coded SSH keys. Use secret management tools for Puppet such as Hiera',
                     line:    value_token.line,
                     column:  value_token.column,
                     token:   value_token
                  }
               end
           end
       end
  end

end
