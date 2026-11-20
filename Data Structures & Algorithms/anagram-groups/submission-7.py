class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final = [[str]]
        stringval = {}
        for string in strs:
            letters = [0]*26
            for char in string:
                letters[ord(char)-97] +=1
            if stringval.get(tuple(letters), -1)== -1:
                stringval[tuple(letters)]=[string]
            else:
                stringval.get(tuple(letters)).append(string)
        return list(stringval.values())