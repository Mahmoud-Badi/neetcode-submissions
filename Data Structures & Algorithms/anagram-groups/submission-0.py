class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDict = defaultdict(list) # groups keyed by letter count

        for s in strs:
            count = [0] * 26 # letter counts, a-z

            for char in s:
                count[ord(char) - ord("a")] += 1 # bump this letter's count

            key = tuple(count) # lists can't be dict keys, tuples can
            anagramDict[key].append(s) # same counts = same group
        
        return list(anagramDict.values()) # prints all the groups 

        # Time = O(n*m), Space = O(n*m)