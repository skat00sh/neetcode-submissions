class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sorted_list = sorted(nums)
        found_dup = False
        for i in range(len(sorted_list)-1):
            if sorted_list[i] == sorted_list[i+1]:
                return True
                exit()
    
        return False