class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1

        sorted_items = sorted(hashmap.items(), key=lambda x: x[1], reverse=True)

        ans = []
        for i in range(k):
            ans.append(sorted_items[i][0])

        return ans