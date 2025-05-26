class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()

        for email in emails:
            localName, domainName = email.split('@')
            localName = localName.replace('.', '')
            localName = localName.split('+')[0]

            normalized_email = localName + '@' + domainName

            unique_emails.add(normalized_email)
        return len(unique_emails)


