
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        dics={}

        for words in strs:

            key="".join(sorted(words))
            
            if key in dics:

                dics[key].append(words)
            else:
                dics[key]=[words]
        return list(dics.values())
           
