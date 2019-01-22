'''
Akond Rahman 
Rule to detect weak cryptography algorithms: MD5/SHA1 
Jan 21, 2019 
'''

from ansiblelint import AnsibleLintRule

class WeakCryptoRule(AnsibleLintRule):
    id = 'SECURITY:::MD5:::'
    shortdesc = 'Weak crypto. algo.'
    description = 'Check for weak cryptography algorithms'
    tags = { 'security' }

    def match(self, file, line):
        if '#' not in line:
            line = line.lower()
            if ( ('md5' in line) or ('sha1' in line) ): 
                print 'SECURITY:::MD5:::Do not use MD5 or SHA1, as they have security weakness. Use SHA-512.'  