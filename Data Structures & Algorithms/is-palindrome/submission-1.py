class Solution:
    def isPalindrome(self, s: str) -> bool:
        palindrome=True
        s=s.replace(" ","")
        for char in s:
            if not char.isalnum():
                s=s.replace(char,"")
        s=s.lower()
        for i in range(len(s)//2):
            if s[i]!=s[len(s)-i-1]:
                    palindrome=False
                    break
        return palindrome


