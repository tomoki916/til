function zigzagLevelOrder(root: TreeNode | null): number[][] {
  if (!root) return [];
  const result: number[][] = [];
  const queue = [];
  queue.push(root);

  while (queue.length > 0) {
    const queueLength = queue.length;
    result.push([]);
    for (let i = 0; i < queueLength; i++) {
      let currentNode = queue.shift() as TreeNode;
      result[result.length - 1].push(currentNode.val);
      if (currentNode?.left) queue.push(currentNode.left);
      if (currentNode?.right) queue.push(currentNode.right);
    }
    if (result.length % 2 == 0) result[result.length - 1].reverse();
  }

  return result;
}
