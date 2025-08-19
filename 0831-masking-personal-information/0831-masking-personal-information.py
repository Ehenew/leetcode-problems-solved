class Solution:
    def maskPII(self, s: str) -> str:

        if '@' in s:  
            s = s.lower()
            name, domain = s.split('@')
            masked_name = name[0] + '*' * 5 + name[-1]
            return masked_name + '@' + domain
        else:
            digits = [ch for ch in s if ch.isdigit()]
            local = "***-***-" + "".join(digits[-4:])
            country_code_len = len(digits) - 10
            if country_code_len > 0:
                return "+" + "*" * country_code_len + "-" + local
            else:
                return local

            