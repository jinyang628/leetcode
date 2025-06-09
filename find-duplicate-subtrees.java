final String encoded = root.val + "#" + encode(root.left, count,ans)
 + "#" + encode(root.right, count, ans);