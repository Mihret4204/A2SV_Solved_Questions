class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        ans=[]
        count={}
        for i,cpdomain in enumerate(cpdomains):
            domains_list=cpdomain.split()
            num=int(domains_list[0])

            domains=domains_list[1].split(".")
            for j in range(len(domains)):
                subdomain= ".".join(domains[j:])
                count[subdomain] = count.get(subdomain, 0) + num
        for subdomains,total in count.items():
            ans.append(f"{total} {subdomains}")
        return ans


        