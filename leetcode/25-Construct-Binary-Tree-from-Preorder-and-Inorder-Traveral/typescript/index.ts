function buildTree(preorder: number[], inorder: number[]): TreeNode | null {
  if (preorder.length === 0 || inorder.length === 0) return null;
  const rootVal = preorder[0];
  const node = new TreeNode(rootVal);

  const rootIndex = inorder.indexOf(rootVal); // この値が左のsubtreeの個数に対応する
  const leftInorder = inorder.slice(0, rootIndex);
  const rightInorder = inorder.slice(rootIndex + 1);

  const leftPreorder = preorder.slice(1, 1 + rootIndex);
  const rightPreorder = preorder.slice(1 + rootIndex);

  node.left = buildTree(leftPreorder, leftInorder);
  node.right = buildTree(rightPreorder, rightInorder);

  return node;
}
