class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ["a", "e", "i", "o", "u"]
        i = 0
        j = len(s) - 1
        s = list(s)
        while i < j:
            if s[i].lower() in vowels and s[j].lower() in vowels:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
            elif s[i].lower() in vowels:
                j -= 1
            elif s[j].lower() in vowels:
                i += 1
            else:
                i += 1
                j -= 1
        return "".join(s)
                    

        