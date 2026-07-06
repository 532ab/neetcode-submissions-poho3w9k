class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique_numbers = set(nums)
        longest_streak = 0

        # Loop through unique numbers to avoid redundant checks
        for num in unique_numbers:
            
            # Only start counting if 'num' is the absolute beginning of a sequence
            is_sequence_start = (num - 1) not in unique_numbers
            
            if is_sequence_start:
                current_streak = 1
                
                # Look ahead by adding the current streak to the starting number
                while (num + current_streak) in unique_numbers:
                    current_streak += 1
                
                # Update the record high score
                longest_streak = max(current_streak, longest_streak)
                
        return longest_streak