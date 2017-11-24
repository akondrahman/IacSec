=begin
Gathered from the itnernet, to extend puppet-lint
will be used as reff.  
=end
PuppetLint.new_check(:no_file_path_attribute) do

  def check
    resource_indexes.each do |resource|
      if resource[:type].value == 'file'
        resource[:param_tokens].select { |param_token|
          param_token.value == 'path'
        }.each do |param_token|
          value_token = param_token.next_code_token.next_code_token

          notify :warning, {
            message: 'file resources should not have a path attribute. Use the title instead',
            line:    value_token.line,
            column:  value_token.column,
            token:   value_token
          }
        end
      end
    end
  end

end
