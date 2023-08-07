#Problem statement: Every valid email consists of a local name and a domain name, separated by the '@' sign. Besides
#lowercase letters, the email may contain one or more '.' or '+'.

#For example, in "alice@leetcode.com", "alice" is the local name, and "leetcode.com" is the domain name.
#If you add periods '.' between some characters in the local name part of an email address, mail sent there will be
#forwarded to the same address without dots in the local name. Note that this rule does not apply to domain names.

#For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.
#If you add a plus '+' in the local name, everything after the first plus sign will be ignored. This allows certain
#emails to be filtered. Note that this rule does not apply to domain names.

#For example, "m.y+name@email.com" will be forwarded to "my@email.com".
#It is possible to use both of these rules at the same time.

#Given an array of strings emails where we send one email to each emails[i], return the number of different
#addresses that actually receive mails.

class Solution:
    def numUniqueEmails(self, emails):
    #Creating a set in which we can add the emails after removing . and ignoring string + in localname
        unique_emails = set()

    #Iterating over every email and changing localname by ignoring . and characters after +. We can then create
    #localname. Domain_name can be created by slicing list from @ symbol
        for email in emails:
            local_name = ""
            i = 0
            while email[i] not in ['@', '+']:
                if email[i] != '.':
                    local_name += email[i]
                i += 1
            
            while email[i] != '@':
                i += 1
        #Creating domain name and concatenating localname+domain to form the complete email address and storing it
        # hashSet to eliminate duplicity.   
            domain_name = email[i:]
            unique_emails.add(local_name+domain_name)
        
        return len(unique_emails)
        
#Testcases:
emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
print(Solution().numUniqueEmails(emails))

emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
print(Solution().numUniqueEmails(emails))