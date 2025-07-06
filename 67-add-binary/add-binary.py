class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        deci1=0
        deci2=0
        bin1=""
        sum1=0
        if a=='0' and b=='0':
            return '0'
        else:
        
            for i in range(len(a)):
                e=len(a)-1-i
                deci1=deci1+int(a[i])*2**e

            for i in range(len(b)):
                e=len(b)-1-i
                deci2=deci2+int(b[i])*2**e

            sum1=deci1+deci2
            print(deci1,deci2,sum1)

            while sum1>1:
                bin1=bin1+str((sum1)%2)
                sum1=(sum1)/2
            bin1=bin1+'1'

            return bin1[::-1]
