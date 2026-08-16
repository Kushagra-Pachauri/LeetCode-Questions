from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words:
            return []

        w = len(words[0])
        total = w * len(words)
        target = sorted(words)
        ans = []

        for i in range(len(s) - total + 1):
            parts = []
            for j in range(0, total, w):
                parts.append(s[i + j:i + j + w])
            if sorted(parts) == target:
                ans.append(i)

        return ans