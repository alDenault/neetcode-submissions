class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final = [[str]]
        stringval = {}
        for string in strs:
            letters = [0]*26
            for char in string:
                letters[ord(char)-97] = letters[ord(char)-97]+1
            stringtotal = ','.join(str(x) for x in letters)
            if stringval.get(stringtotal, -1)== -1:
                stringval[stringtotal]=[string]
            else:
                stringval.get(stringtotal).append(string)
        return list(stringval.values())