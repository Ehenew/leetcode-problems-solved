class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counter = {}

        for cp in cpdomains:
            count, domain = cp.split()
            count = int(count)
            parts = domain.split('.')

            for i in range(len(parts)):
                sub = ".".join(parts[i:])
                counter[sub] = counter.get(sub, 0) + count

        return [f"{cnt} {dom}" for dom, cnt in counter.items()]
