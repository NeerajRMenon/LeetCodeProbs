class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        flag=0
        if len(nums)==1:
            return nums[0]
        elif len(nums)==0:
            return null
        for i in nums:
            list1=nums[:]
            list1.remove(i)
            for j in list1:
                if j!=i:
                    flag=1
                else:
                    continue
            if flag==1:
                return i
                """
        
        for i in nums:
            list1=nums[:]
            list1.remove(i)
            if i not in list1:
                return i

        