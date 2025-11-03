#len of last word


class Solution(object):
    def lengthOfLastWord(self, s):
        a=s.split()
        return len(a[-1])

#plus one

class Solution(object):
    def plusOne(self, digits):
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0


        return [1] + digits
