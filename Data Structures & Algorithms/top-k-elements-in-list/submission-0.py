class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        kfreq = []
        for num in nums:
            if num in freq:
                freq[num] = freq[num] + 1
            else:
                freq[num] = 1
        soreted_freq = dict(sorted(freq.items(), key=lambda items:items[1], reverse=True))
        return list(soreted_freq)[:k]