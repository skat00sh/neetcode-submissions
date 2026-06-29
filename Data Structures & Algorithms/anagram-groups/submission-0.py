class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = [[strs[0]]]
        for str in strs[1:]:       
            found = False
            for r in result:
                if sorted(r[0]) == sorted(str):
                    r.append(str)
                    found = True
                
            if not found:
                new_entry = [str]
                result.append(new_entry)
                found = False
                    
        
        return result