class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # write code here
        if len(s) == 0 and len(pattern) == 0:
            return True
        if len(s) > 0 and len(pattern) == 0:
            return False
        # 如果模式第二个字符是*
        if len(pattern) > 1 and pattern[1] == '*':
            if len(s) > 0 and (s[0] == pattern[0] or pattern[0] == '.'):
                # 如果第一个字符匹配，三种可能1、模式后移两位；2、字符串移1位
                return self.match(s, pattern[2:]) or self.match(s[1:], pattern)
            else:
                # 如果第一个字符不匹配，模式往后移2位，相当于忽略x*
                return self.match(s, pattern[2:])
        # 如果模式第二个字符不是*
        if len(s) > 0 and (s[0] == pattern[0] or pattern[0] == '.'):
            return self.match(s[1:], pattern[1:])
        else:
            return False