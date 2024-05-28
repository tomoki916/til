function sortedArrayToBST(nums: number[]): TreeNode | null {
  if (nums.length == 0) return null;

  const center = Math.floor(nums.length / 2);
  const root = nums[center];

  const node = new TreeNode(root);
  node.left = sortedArrayToBST(nums.slice(0, center));
  node.right = sortedArrayToBST(nums.slice(center + 1));

  return node;
}
