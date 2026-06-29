class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        while i <= len(nums) - 2:
            j = len(nums) - 1
            while j > i:
                print (i,j)
                if (nums[i] + nums[j]) == target:
                    return [i,j]
                else:
                    j = j - 1            
            i = i+1