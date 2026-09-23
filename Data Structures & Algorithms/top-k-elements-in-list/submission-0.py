class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencyMap = {}

        for num in nums:
            frequencyMap[num] = 1 + frequencyMap.get(num, 0)

        # sort (number, count) pairs by count, highest first
        sortedPairs = sorted(frequencyMap.items(), key=lambda pair: pair[1], reverse=True)

        # take the top k pairs, then pull out just the number from each
        topK = sortedPairs[:k]
        return [pair[0] for pair in topK]