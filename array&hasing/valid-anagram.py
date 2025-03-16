# Given two strings s and t, 
# return true if the two strings are anagrams of each other, 
# otherwise return false.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# s = "khanhnh", t = "hnhnahk" -> True
# s = "nhk", t = "kkk" -> False

class Solution:
    def anAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)
    
def main():
    slt = Solution()
    s = "khanhnh"
    t = "hnhnahk"
    result = slt.anAnagram(s, t)
    print(result)

if __name__ == "__main__":
    main()

#comment: sử dụng bảng băm có thuộc tính get()