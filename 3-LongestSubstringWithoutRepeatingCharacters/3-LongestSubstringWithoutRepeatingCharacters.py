class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right, best = 0, 0, 1
        seen = set()

        if len(s) == 0:
            return 0

        while right < len(s):
            if s[right] not in seen:
                seen.add(s[right])
                right += 1
                
            else:
                best = max(best, right - left)
                seen.remove(s[left])
                left += 1

        return max(best, right - left)
