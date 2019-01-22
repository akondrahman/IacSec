'''
Akond Rahman 
Rule to detect suspicious comments 
Jan 21, 2019 
'''

from ansiblelint import AnsibleLintRule

class HTTPRule(AnsibleLintRule):
    id = 'SECURITY:::HTTP:::'
    shortdesc = 'HTTP without TLS'
    description = 'Check for use for HTTP without TLS'
    tags = { 'security' }

    def match(self, file, line):
        if ( ('#' not in line) and (':' in line) ):
            line = line.lower()
            attr = line.split(':')[0]
            if (len(attr) > 0):
               if ( 'http://' in line ): 
                  print 'SECURITY:::HTTP:::Do not use HTTP without TLS. This may cause a man in the middle attack. Use TLS with HTTP'  