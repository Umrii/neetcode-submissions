class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = {}

        # Count frequencies
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # Sort keys based on their frequency
        sorted_nums = sorted(freq, key=freq.get, reverse=True)

        # Return top k frequent elements
        return sorted_nums[:k]