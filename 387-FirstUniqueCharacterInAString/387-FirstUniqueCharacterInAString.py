class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}

        for i in range(len(s)):
            count[s[i]] = count.get(s[i], [])
            count[s[i]].append(i)

        for val in count.values():
            if len(val) == 1:
                return val[0]
        return -1
