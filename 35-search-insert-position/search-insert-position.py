class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        x=0
        for i in range(len(nums)):
            if nums[i]==target:
                x=i
            elif (i+1)<len(nums) and nums[i]<=target<=nums[i+1]:
                x=i+1
            elif (i+1)<len(nums) and nums[len(nums)-1]<target:
                x=len(nums)
                
            elif (i)<len(nums) and nums[len(nums)-1]<target:
                x=len(nums)

        return x