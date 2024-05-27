// function isValidBST(root: TreeNode | null): boolean {
//   if (!root) return true;

//   const isValid = (
//     rootValue: number,
//     node: TreeNode,
//     side: "right" | "left"
//   ): boolean => {
//     if (node.left !== null && node.left.val >= node.val) return false;
//     if (node.right !== null && node.right.val <= node.val) return false;
//     if (side === "left" && node.val >= rootValue) return false;
//     if (side === "right" && node.val <= rootValue) return false;

//     const isValidLeft =
//       node.left !== null ? isValid(rootValue, node.left, side) : true;
//     const isValidRight =
//       node.right !== null ? isValid(rootValue, node.right, side) : true;

//     return isValidLeft && isValidRight;
//   };

//   const isValidLeft =
//     root.left !== null
//       ? isValid(root.val, root.left, "left") && isValidBST(root.left)
//       : true;
//   const isValidRight =
//     root.right !== null
//       ? isValid(root.val, root.right, "right") && isValidBST(root.right)
//       : true;
//   return isValidLeft && isValidRight;
// }
function isValidBST(
  root: TreeNode | null,
  min = -Infinity,
  max = Infinity
): boolean {
  if (!root) return true;

  if (max <= root.val || min >= root.val) return false;

  return (
    isValidBST(root.left, min, root.val) &&
    isValidBST(root.right, root.val, max)
  );
}
