class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"

        for _ in range(n - 1):
            res = ""
            i = 0

            while i < len(s):
                j = i

                while j < len(s) and s[j] == s[i]:
                    j += 1

                res += str(j - i) + s[i]
                i = j

            s = res

        return s