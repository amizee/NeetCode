class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = [0] * 26
        for c in s1:
            s1_count[ord(c) - ord('a')] += 1
 
        s2_count = [0] * 26
        l = 0
        for r in range(len(s2)):
            s2_count[ord(s2[r]) - ord('a')] += 1
            if (r - l + 1) == len(s1) and s1_count == s2_count:
                return True
            if (r - l + 1) == len(s1):
                s2_count[ord(s2[l]) - ord('a')] -= 1
                l += 1
        return False
    
# Intuition: keep a frequency count using an array of size 26 so it is comparable and still O(1) space. Keep a fixed size window of the smaller substring and at each iteration, check if the two counts match.

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1
        return matches == 26

# Similar intuition but solution is more robust, no need to check (count - 2) or more because this letter has already been determined to not be a match so you don't want to further decrease the matches.