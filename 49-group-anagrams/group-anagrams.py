class Solution:
    # take string one bye one convert into list and sort
    def is_sorted(self,s):
        s1=list(s)
        s1.sort()
        return "".join(s1)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1={} 
        for s in strs:
            key=self.is_sorted(s)
            if key in dict1: #if present append in that list
                dict1[key].append(s)
            else: # not present create new list
                dict1[key]=[s]    
        return list(dict1.values())   #resturn the map after converting to list

        