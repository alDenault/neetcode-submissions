class Solution:

    def encode(self, strs: List[str]) -> str:
        length = len(strs)
        encoded = str(length)+','
        for string in strs:
            encoded = encoded + str(len(string)) +','+ string
        return encoded
    def decode(self, s: str) -> List[str]:
        encoded = s
        lengthmark = encoded.index(',')
        length = int(encoded[0:lengthmark])
        encoded = encoded[lengthmark+1:len(encoded)]
        stringlist = []
        for i in range(0,length):
            stringlengthmark=encoded.index(',')
            stringlength = int(encoded[0:stringlengthmark])
            stringlist.append(encoded[stringlengthmark+1:stringlengthmark+stringlength+1])
            encoded = encoded[stringlengthmark+stringlength+1:len(encoded)]
        return stringlist