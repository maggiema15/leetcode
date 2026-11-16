class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split()
        rsp = []
        for i in range(len(arr) -1, - 1, - 1):
            rsp.append(arr[i])

        return (" ").join(rsp)
