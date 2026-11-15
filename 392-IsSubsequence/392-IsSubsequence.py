class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        s_ptr = 0
        
        for i in range(len(t)):
            if s_ptr == len(s):
                return True
            if s[s_ptr] == t[i]:
                s_ptr += 1

        if s_ptr != len(s):
            return False
        
        return True
