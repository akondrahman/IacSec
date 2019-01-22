'''
Akond Rahman 
Rule to detect binding to 0.0.0.0 
Jan 21, 2019 
'''

from ansiblelint import AnsibleLintRule

class InvalidBindingRule(AnsibleLintRule):
    id = 'SECURITY:::BINDING_TO_ALL:::'
    shortdesc = 'Binding to 0.0.0.0'
    description = 'Check for use for binding to 0.0.0.0'
    tags = { 'security' }

    def match(self, file, line):
        if ( ('#' not in line) and (':' in line) ):
            line = line.lower()
            attr = line.split(':')[0]
            if (len(attr) > 0):
               if ( '0.0.0.0' in line ): 
                  print 'SECURITY:::BINDING_TO_ALL:::Do not bind to 0.0.0.0. This may cause a DDOS attack. Restrict your available IPs.'  