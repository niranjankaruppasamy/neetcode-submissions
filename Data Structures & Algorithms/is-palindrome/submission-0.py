class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        return re.sub('[^0-9a-zA-Z]+', '', s).lower() == re.sub('[^0-9a-zA-Z]+', '', s[::-1]).lower()