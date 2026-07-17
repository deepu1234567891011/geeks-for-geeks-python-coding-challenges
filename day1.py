class Solution:
    def checkStatus(self, a, b, flag):
        # code here
        if flag:
            if a<0 and b<0:
                return True
        else:
            if(a>=0 and b<0)or(a<0 and b>=0):
                return True
            return False
obj=Solution()
print(obj.checkStatus(-1,-2,True))