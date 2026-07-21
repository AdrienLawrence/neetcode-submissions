class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = []
        used = []
        for i, string in enumerate(strs):
            strlist = [string]
            mark = sorted(string)
            if mark in used:
                continue
            used.append(mark)
            for j, string2 in enumerate(strs):
                sort2 = sorted(string2)
                if mark == sort2 and i != j:
                    strlist.append(string2)
            groups.append(strlist)
        return groups
        