
def permute(nums):
    # List to store the result
    result = []
    
    # Helper function for backtracking
    def backtrack(curr_permutation, remaining_nums):
        # Base case: If there are no remaining numbers, the current permutation is complete
        if len(remaining_nums) == 0:
            result.append(curr_permutation)
            return
        
        # Recursive case: Try all possible choices for the next number
        for i in range(len(remaining_nums)):
            # Make a choice
            num = remaining_nums[i]
            next_permutation = curr_permutation + [num]
            remaining = remaining_nums[:i] + remaining_nums[i+1:]
            
            # Recursively explore the remaining choices
            backtrack(next_permutation, remaining)
    
    # Start the backtracking process
    backtrack([], nums)
    
    return result
