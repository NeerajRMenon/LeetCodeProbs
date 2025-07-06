class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
             
        """
        #neeraj
        str2=""
        list1=[]
        for i in digits:
            str2=str2+str(i)
        int1=int(str2)
        int1+=1
        str2=str(int1)
        for i in str2:
            list1.append(int(i))
        return list1
