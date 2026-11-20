class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapS = {}
        mapT = {}
        for char in s: 
            if mapS.get(char, -1) == -1:
                mapS[char]=1
            else:
                mapS[char]=mapS.get(char,0)+1
        for char in t: 
            if mapT.get(char, -1) == -1:
                mapT[char]=1
            else:
                mapT[char]=mapT.get(char,0)+1
        if mapS==mapT:
            return True
        else:
            return False
