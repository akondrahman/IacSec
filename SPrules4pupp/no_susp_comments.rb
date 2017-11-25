=begin
Akond Rahman
Nov 24, 2017
Friday
Detect anti-pattern: suspicous comments
=end
PuppetLint.new_check(:no_hardcode_key) do

  def check
     ##for comments we need to grab all lines
     lineNo=0
     manifest_lines.each do |single_line|
        ##first check if string starts with #, which is comemnt in Puppet
        if single_line.include? '#'
           lineNo += 1
           ### check if those keywords exist
           single_line=single_line.downcase
           if (single_line.include?('bug') || single_line.include?('hack') || single_line.include?('fixme') || single_line.include?('later') || single_line.include?('later2') || single_line.include?('todo'))
              print "#{single_line} #{lineNo}\n"
              print "-----\n"
           end
        end
     end
  end
end
