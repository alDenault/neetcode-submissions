class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if freq.get(num, -1) == -1:
                freq[num]=1
            else: 
                freq[num]=freq[num]+1
        answer = []
        for i in range(0,k):
            answer.append(max(freq, key=freq.get))
            freq.pop(max(freq, key=freq.get))
        return answer