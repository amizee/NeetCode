class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqs = {}
        maxF = 0
        res = 0

        l = 0
        for r in range(len(s)):
            freqs[s[r]] = freqs.get(s[r], 0) + 1
            maxF = max(freqs[s[r]], maxF)
        
            while (r - l + 1) - maxF > k:
                freqs[s[l]] -= 1
                maxF = max(freqs[s[l]], maxF) # Technically don't need this because maxF will always be smaller than the highest maxF so far, meaning the length of the substring cannot be higher
                l += 1
            res = max(r - l + 1, res)
        return res

# Intuition: Keep track of the maximum frequency of any letter for the current substring - minimises replacements. If we cannot replace all the letters, we reduce the size of the substring until we can.
