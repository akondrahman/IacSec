=begin
Akond Rahman
Nov 24, 2017
Friday
Detect anti-pattern: suspicous comments
=end
PuppetLint.new_check(:no_hardcode_key) do

  def check
     ##for comments we need to grab all lines
     manifest_lines.each do |single_line|
        ##first check if string starts with #, which is comemnt in Puppet
        if single_line.start_with?('#')
           print "#{single_line}"
        end
     end
  end
end
