class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        currSubstring = set()
        maxLength = 0
        l, r = 0, 0
        while r < len(s):
            while s[r] in currSubstring:
                currSubstring.remove(s[l])
                l += 1
            currSubstring.add(s[r])
            maxLength = max(len(currSubstring), maxLength)
            r += 1
        
        return maxLength

# Intuition: keep a set of unique characters for the current substring. If we find a duplicate, we have to remove all characters until we reach the duplicate inclusive.
# l and r represent the left and right of the current substring