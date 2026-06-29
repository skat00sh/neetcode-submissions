class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #sorted_list = sorted(nums)
        #found_dup = False
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
                exit()
    
        return False