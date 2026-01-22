class Solution:

    def encode(self, strs: List[str]) -> str:
        msg = ""
        for s in strs:
            msg += str(len(s)) + "#" + s
        return msg

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            i, j = j + 1, j + length + 1
            word = s[i:j]
            res.append(word)
            i = j
                
        return res

# Intuition: encode each string using a delimiter and the length of the string. When decoding loop until you find the delimiter, giving you the length of the current word.