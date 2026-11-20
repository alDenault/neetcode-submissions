class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final = [[str]]
        stringval = {}
        for string in strs:
            letters = [0]*26
            for char in string:
                letters[ord(char)-97] = letters[ord(char)-97]+1
            letters = tuple(letters)
            if stringval.get(letters, -1)== -1:
                stringval[letters]=[string]
            else:
                stringval.get(letters).append(string)
        return list(stringval.values())