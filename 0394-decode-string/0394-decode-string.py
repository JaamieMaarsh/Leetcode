class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        for c in s:
            if c != "]" :
                stack.append(c)
            else:
                current_string = ""
                while stack[-1] != "[":
                    current_string = stack.pop() + current_string
                stack.pop()
                
                num = ""
                while stack and stack[-1] .isnumeric():
                    num = stack.pop() + num
                
                stack.append(int(num)*current_string)
            
        return ''.join(stack)
