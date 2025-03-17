# Given a string s, 
# return true if it is a palindrome, 
# otherwise return false.

# s = "Was it a car or a cat I saw?" -> True
# s = "tab a cat" -> False

class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ''
        for c in s:
            if c.isalnum():
                new_s += c.lower()
        return new_s == new_s[::-1]
    
def main():
    slt = Solution()
    s = "Was it a car or a cat I saw?"
    result = slt.isPalindrome(s)
    print(result)

if __name__ == "__main__":
    main()