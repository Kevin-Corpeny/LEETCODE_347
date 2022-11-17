from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countmap = {}
        nodupes = set(nums)
        for x in sorted(nodupes):
            countmap[x] = nums.count(x)
        sorted_pairs = sorted(countmap.items(), key=lambda x: x[1])
        print(sorted_pairs)
        ans = []
        for val in sorted_pairs[-1:-k-1:-1]:
            ans.append(val[0])
        return ans
    
    
sol = Solution()
print(sol.topKFrequent([1,1,1,3,3,2,2,2,6,5],2)) #should print [1,2]

#LOL THIS MUST BE THE DUMBEST WAY TO DO THIS
