class Solution(object):
    def singleNumber(self, nums):
     
        for i in nums:
            list1=nums[:]
            list1.remove(i)
            if i not in list1:
                return i

        