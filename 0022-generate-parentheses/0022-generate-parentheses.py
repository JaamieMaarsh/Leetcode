class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        result = []
        
        def backtracking(open_paranthesis, close_paranthesis):
            if open_paranthesis == close_paranthesis == n:
                result.append("".join(stack)) # the "" joins the parathesis together and appends them to the result string
                return
            
            if open_paranthesis < n:
                stack.append("(")
                backtracking(open_paranthesis + 1, close_paranthesis)
                stack.pop()
                
            if close_paranthesis < open_paranthesis:
                stack.append(")")
                backtracking(open_paranthesis, close_paranthesis + 1)
                stack.pop()
                
        backtracking(0,0)
        return result
                