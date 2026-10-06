class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums) # removes duplicates, gives O(1) lookup instead of O(n)
        longest = 0 # best sequence length found so far

        for num in numSet:
            # only start counting if num is the START of a sequence
            # if num-1 exists, some earlier number will handle this run instead
            if (num - 1) not in numSet:
                length = 0
                while (num + length) in numSet: # keep extending while the next number exists
                    length += 1

                # keep whichever is bigger, new run or old record
                if length > longest:
                    longest = length

        return longest

        # Time = O(n): every number only gets counted by the while loop once, across the whole run
        # Space = O(n) for the set