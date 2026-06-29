class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != len(t):
        #     return False
        # else:
        #     if sorted(s) == sorted(t):
        #         return True
        #     else:
        #         return False
        return sorted(s) == sorted(t)
                


        