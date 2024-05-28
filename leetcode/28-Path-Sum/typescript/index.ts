function hasPathSum(root: TreeNode | null, targetSum: number): boolean {
  if (!root) return false;

  if (!root.left && !root.right && root.val == targetSum) return true;

  return (
    hasPathSum(root.left, targetSum - root.val) ||
    hasPathSum(root.right, targetSum - root.val)
  );
}
