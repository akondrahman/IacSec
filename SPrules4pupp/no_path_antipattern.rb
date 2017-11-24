=begin
Akond Rahman
Nov 24, 2017
See if path values contain the anti-pattern contains drive letter 
=end
PuppetLint.new_check(:no_hardcode_key) do

  def check
           ### with resources we miss some path, so grab all tokens,a nd check them one-by-one
           tokens.each do |value_token|
               token_val_str = value_token.value
               path_sym_cnt1  = token_val_str.count('/')
               path_sym_cnt2  = token_val_str.count('\\')
               ##first check if value is a directory or file, if valeu contains at least two slashes then proceed
               if path_sym_cnt1 > 1 or path_sym_cnt2 > 1
                  token_val_str=token_val_str.downcase
                  if token_val_str.include? "c:"
                     notify :warning, {
                        message: 'Do not use Windows drive letters in path',
                        line:    value_token.line,
                        column:  value_token.column,
                        token:   value_token
                     }
                  end
               end
           end
  end
end
