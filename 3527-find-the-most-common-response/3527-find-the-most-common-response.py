class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        res_map={}
        for i in range(len(responses)):
            res_set=set(responses[i])
            for res in res_set:
                res_map[res]=res_map.get(res,0)+1
        
        mapp=sorted(res_map.keys())
        max_count=0
        result = ""
        for val in mapp:
            if res_map[val]>max_count:
                max_count=res_map[val]
                result=val
        return result
                  
