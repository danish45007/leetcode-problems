class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        # split the path by '/'
        path = path.split("/")
        for p in path:
            # pop out recently add filename from stack by popping out the top
            if stack and p == "..":
                stack.pop()
            # add filename only into stack 
            if (p != "." and p != ".." and len(p) > 0):
                stack.append(p)
        # prepend "/" into the result and join the filename in stack by "/"
        return "/" + "/".join(stack)