class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == '[' or i=='(' or i=='{':
                stack.append(i)
                continue
            else:
                if i==')':
                    if len(stack)==0 or stack[-1]!='(':
                        return False
                    else:
                        stack.pop()
                if i==']':
                    if len(stack)==0 or stack[-1]!='[':
                        return False
                    else:
                        stack.pop()
                if i=='}':
                    if len(stack)==0 or stack[-1]!='{':
                        return False
                    else:
                        stack.pop()
        return len(stack)==0    