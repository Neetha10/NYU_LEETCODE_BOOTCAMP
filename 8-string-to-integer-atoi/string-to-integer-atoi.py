class Solution:
    def myAtoi(self, s: str) -> int:
        i=0
        result=0
        sign=1
        length=len(s)

        while i<length and s[i]==" ":
            i+=1
        if i<length:
            if s[i]=='+':
                sign=1
                i+=1
            elif s[i]=='-':
                sign=-1
                i+=1
        while i<length and s[i].isdigit():
            digit=int(s[i])
            if result>214748364 or (result == 214748364 and digit >7):
                return 2147483647 if sign==1 else -2147483648


            result=result*10+int(s[i])
            i+=1
        return sign * result




            
