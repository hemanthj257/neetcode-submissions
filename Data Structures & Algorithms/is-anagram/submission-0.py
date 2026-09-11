class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l1 = [0] * 26
        l2 = [0] * 26

        for i in range(len(s)):
            pos = ord(s[i]) - ord('a')
            l1[pos] = l1[pos] + 1

        for i in range(len(t)):
            pos = ord(t[i]) - ord('a')
            l2[pos] = l2[pos] + 1

        is_anagram, j = True, 0
        while j < len(l1) and is_anagram:
            if l1[j] == l2[j]:
                j += 1
            else:
                is_anagram = False
        
        return is_anagram