class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Initialize a list of zeros with the same length as temperatures
        ans = [0] * len(temperatures)
        stack = []  # This will store pairs of (temperature, index)
        
        for curr_idx, curr_temp in enumerate(temperatures):
            # While the stack is not empty and the current temperature is warmer
            # than the temperature at the top of our stack...
            while stack and curr_temp > stack[-1][0]:
                pop_temp, pop_idx = stack.pop()
                # Calculate how many days we waited
                ans[pop_idx] = curr_idx - pop_idx
            
            # Push the current temperature and its index onto the stack
            stack.append((curr_temp, curr_idx))
            
        return ans