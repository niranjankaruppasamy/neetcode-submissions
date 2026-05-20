class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        heap = []
        temp_arr = []
        temp = {}
        for i in nums:
            if i in temp:
                temp[i] += 1
                continue
            temp[i] = 1
        
        for i, j in temp.items():
            temp_arr.append((-j,i))

        heapq.heapify(temp_arr)
        res = []
        for i in range(k):
            ans = heapq.heappop(temp_arr)
            res.append(ans[1])
        return res