class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate_map = set()
        for i in nums:
            if i not in duplicate_map:
                duplicate_map.add(i)
                continue
            return True
        return False
            
        