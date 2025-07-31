class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        open_brackets=['(','{','[']
        closed_brackets=[')','}',']']
        for i in s:
            if i in open_brackets:
                stack.append(i)
            elif i in closed_brackets:
                if not stack:
                    return False
                if open_brackets[closed_brackets.index(i)] !=stack[-1]:
                    return False
                stack.pop()
        return not stack

                    

        
     