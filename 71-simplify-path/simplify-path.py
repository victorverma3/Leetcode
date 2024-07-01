class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        items = [item for item in path.split("/") if not (item == "" or item == ".")]
        stack = []
        for item in items:
            if item == "..":
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(item)
        
        canon = "/" + "/".join(stack)
        return canon
        