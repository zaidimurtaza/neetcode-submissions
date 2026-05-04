class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        anagram_map = {}

        for i in s:
            anagram_map[i] = anagram_map.get(i, 0) + 1

        for j in t:
            if j not in anagram_map or anagram_map[j] == 0:
                return False
            anagram_map[j] = anagram_map.get(i,0)-1
        return True
