class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""
        for c in s:
            if  (ord("a") <= ord(c) <= ord("z")):
                string = string+c
            elif (ord("A") <= ord(c) <= ord("Z")):
                string = string+c.lower()
            elif (ord('0') <= ord(c) <= ord('9')):
                string = string+c
            else:
                continue
        return string == string[::-1]

