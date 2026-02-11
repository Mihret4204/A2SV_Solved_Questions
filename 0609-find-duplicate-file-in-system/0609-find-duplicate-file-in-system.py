class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_map = {}
        
        for p in paths:
            parts = p.split(' ')
            directory = parts[0]  
            files = parts[1:]    
            
            for f in files:
                name, content = f.split('(')
                content = content[:-1] 
                full_path = directory + "/" + name
                
                if content not in content_map:
                    content_map[content] = []
                content_map[content].append(full_path)
        
        return [group for group in content_map.values() if len(group) > 1]