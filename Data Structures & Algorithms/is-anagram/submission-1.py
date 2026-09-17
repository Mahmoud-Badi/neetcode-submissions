class Solution(object):
    def isAnagram(self, s, t):
        #cant be anagram if they have different num of letters
        if len(s) != len(t):
            return False
        
        # we will be creating a hashmap for each and return t if they're equal
        countS, countT = {}, {}

        for i in range(len(s)): #len of s and t are the same here
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        #now we go through the hashmap so see if they match
        for c in countS:
            if countS[c] != countT.get(c ,0):
                return False
        #if it were able to go through the hashmap and non of them didnt match then True
        return True
 
        '''
        Another way of solving this which doesnt require as much memory:
        return sorted(s) == sorted(t)
        This works as the strings are sorted then they must be identicial
        to be an anagram.   
        '''     
