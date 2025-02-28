class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]* len(temperatures)
        stack = [] # pairwise [(temp, index)]
        #temperatures = [73,74,75,71,69,72,76,73]

        for i, temp in enumerate(temperatures): # if temp = 72
            if stack == [] : # stack = [(75,2), (71,3), (69,4)]
                stack.append([temp,i])
            else:   # stack = [ ]
                while stack and temp > stack[-1][0]: # -1 denotes the 1st element in the stack and 0 denotes the temp value in the stack
                    result[stack[-1][1]] = i - stack[-1][1] # result = [1,0,0,...]
                    stack.pop()
                stack.append([temp,i])
                # if temp < stack[-1][0]:
                #     stack.append([temp,i])
        return result


