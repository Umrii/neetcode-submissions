
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dics=defaultdict(list)
        for word in strs:
            key="".join(sorted(word))
            if key in dics:
                dics[key].append(word)
            else:
                dics[key]=[word]

        return list(dics.values())