class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate_map = {}
        for i in nums:
            if i not in duplicate_map:
                duplicate_map[i] = 1
                continue
            return True
        return False
            
        