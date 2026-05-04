class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        out_ = {}

        for i, ele in enumerate(nums):
            need = target - ele
             
            if need in out_:
                return [out_[need], i]
            
            else: 
                out_[ele] = i

                
            
        