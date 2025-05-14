def dfs(root):
    if root is None:
        return
    if root.left:
        g[root.val].append(root.left.val)
        g[root.left.val].append(root.val)
    if root.right:
        g[root.val].append(root.right.val)
        g[root.right.val].append(root.val)
    dfs(root.left)
    dfs(root.right)