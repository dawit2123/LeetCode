# Problem: Check if One String Swap Can Make Strings Equal - https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/description/

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if Counter(s1)!=Counter(s2):
            return False
        count=0
        for j in range(len(s1)):
            if s1[j]!=s2[j]:
                count+=1
        return count <= 2