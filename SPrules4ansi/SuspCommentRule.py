'''
Akond Rahman 
Rule to detect suspicious comments 
Jan 21, 2019 
'''

from ansiblelint import AnsibleLintRule

class SuspCommentRule(AnsibleLintRule):
    id = 'SECURITY:::SUSPICOUS_COMMENTS:::'
    shortdesc = 'Suspicious comment'
    description = 'Check for suspicious comments'
    tags = { 'security' }

    def match(self, file, line):
        if '#' in line:
            line = line.lower()
            if ( ('hack' in line) or ('fixme' in line) or ('later' in line) or ( 'later2' in line) or ('todo' in line) or ('ticket' in line) or ('bug' in line) or ('to-do' in line) or ('debug' in line ) ): 
                print 'SECURITY:::SUSPICOUS_COMMENTS:::Do not expose sensitive information'  