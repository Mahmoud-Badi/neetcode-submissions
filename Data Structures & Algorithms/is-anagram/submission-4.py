class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # first check if they are the same len
        if len(s) != len(t):
            return False
        
        #now we create hashmaps for each to keep count
        countS = {}
        countT = {}

        #now we build the hashmap
        for i in range(len(s)): # cuz both the same len by now
            countS[s[i]] = 1 + countS.get(s[i], 0) #we add each in the hash map
            #the get is saying if there are non then treat it as 0
            countT[t[i]] = 1 + countT.get(t[i], 0) #now for t

        #now we check
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True
    
    #for python u can just use this:
    #return counter(s) == counter(t) which does the same thing we did but its cheating

    #u can also sort each and if anagram they should be exactly the same
    # return sorted(s) == sorted(t)


