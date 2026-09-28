class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s # length + # + word, combined together
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0 # current position, where this string starts

        while i < len(s):
            j = i # starts with i and will move forward scaning for the #
            while s[j] != "#":
                j += 1

            length = int(s[i:j]) # whatever i is before the # is the length

            result.append(s[j+1 : j+1+length]) # grab exactly `length` chars right after the #
            i = j + 1 + length # move position past this string, to the start of the next one

        return result

        # Time = O(n), Space = O(n)