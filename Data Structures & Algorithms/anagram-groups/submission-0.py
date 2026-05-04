class Solution:
   
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        approch -> is we find one common on the given (condition -> anagram 
        common is the length and the alphabets then 
        we make a common keys > we can use sorted elememt also
        but tomaintain time constrants and given a-z the we make a constant space for 26 
        then we solve -> use it as a key)
        """
        res_ = defaultdict(list)
        
        for ele in strs: 
            res_key = [0] * 26 
            for ch in ele:
                 
                res_key[ord(ch)-ord("a")]+=1

            res_[tuple(res_key)].append(ele)

        return list(res_.values())