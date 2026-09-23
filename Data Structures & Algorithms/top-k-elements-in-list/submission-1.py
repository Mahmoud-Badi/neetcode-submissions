class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # number -> how many times it appeared
        freq = [[] for i in range(len(nums) + 1)] # slots indexed by frequency, freq[i] = numbers that appeared i times

        for num in nums:
            count[num] = 1 + count.get(num, 0) # bump each number's count

        for num, c in count.items():
            freq[c].append(num) # drop each number into its frequency's slot

        result = []
        for i in range(len(freq) - 1, 0, -1): # walk slots from highest frequency down to 1
            for num in freq[i]:
                result.append(num)
                if len(result) == k: # stop as soon as we have k numbers
                    return result

        # Time = O(n), Space = O(n)