class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = s.lower()
        l = 0
        r = len(s)-1
        while r>l:
            if not(string[l].isalnum()):
                l=l+1
            if not(string[r].isalnum()):
                r=r-1
            if (string[l].isalnum()) and (string[r].isalnum()):
                    if string[l]!=string[r]:
                        return False
                    else: 
                        l+=1
                        r+=-1
        return True