class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split("/")
        for p in path:
            if stack and p == "..":
                stack.pop()
            if p.isalnum() or (p != "." and p != ".." and len(p) > 0):
                stack.append(p)
        return "/" + "/".join(stack)