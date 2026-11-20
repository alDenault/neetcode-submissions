class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = s.lower()
        l = 0
        r = len(s)-1
        while r>l:
            lchar=string[l]
            rchar=string[r]
            if not(lchar.isalnum()):
                l=l+1
            if not(rchar.isalnum()):
                r=r-1
            if (lchar.isalnum()) and (rchar.isalnum()):
                    if lchar!=rchar:
                        return False
                    else: 
                        l+=1
                        r+=-1
        return True