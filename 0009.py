class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x >= 0 and x < 10:
            return True
        else:
            old_x = x
            new_x = 0
            while x >= 1:
                new_x *= 10
                new_x += (x % 10)
                x = x // 10
            return new_x == old_x
