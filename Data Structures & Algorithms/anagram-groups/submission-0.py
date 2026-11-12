class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        di = defaultdict(list)

        for s in strs:
            count = [0]*52
            for c in s:
                c_code = ord(c)
                if c_code >= ord('a') and c_code <= ord('z'):
                    count[c_code - ord('a')]+=1
                elif c_code >= ord('A') and c_code <=ord('Z'):
                    count[c_code - ord('A') + 26] += 1
            di[tuple(count)].append(s)
        return list(di.values())

        '''
        learnt:
        - ord() converts char to int
        - defautdict(<type>) creates a dict with automatically assigned 
        default values of type <type>
        - dicts require immutable keys (hence convert list to tuple)
        '''

        
