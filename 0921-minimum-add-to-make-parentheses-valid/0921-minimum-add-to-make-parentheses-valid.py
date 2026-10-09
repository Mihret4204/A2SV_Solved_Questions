class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        st = []
        for c in s:
            
            if c=='(':
                
                st.append('(')
                
                
            else:
                
                if not st:
                    st.append(')')
                elif  st[-1]==')':
                    st.append(')')
                else:
                    st.pop()
            
       
        return len(st)