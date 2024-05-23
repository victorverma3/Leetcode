class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        s = ""
        c = chars[0]
        length = 0
    
        for char in chars:
            if char == c:
                length += 1
            else:
                if length == 1:
                    s += c
                else:
                    s = s + c + str(length)
                c = char
                length = 1
        if length == 1:
            s += c
        else:
            s = s + c + str(length)
            
        chars[:] = list(s)
        return len(chars)