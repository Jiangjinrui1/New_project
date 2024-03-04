class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # self.nums=nums
        # self.target=target
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]
                
        return []
# if'_name_'=="_main_":
nums=[3,3]
target=6
index=Solution().twoSum(nums,target)
print(index)
