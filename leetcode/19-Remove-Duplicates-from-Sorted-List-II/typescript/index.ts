class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

export const convertListNodeToList = (l: ListNode | null): number[] => {
  if (!l) return [];
  const result = new Array<number>();

  let currentNode = l;
  let next = true;
  while (next) {
    if (!currentNode.next) {
      next = false;
    }
    if (currentNode?.val !== undefined) {
      result.push(currentNode.val);
    }
    if (currentNode.next) {
      currentNode = currentNode.next;
    }
  }

  return result;
};

export const convertListToListNode = (l: number[]): ListNode | null => {
  if (l.length === 0) return null;

  const head = l[0];
  if (l.length === 1) return new ListNode(head, null);
  const rest = l.slice(1);
  return new ListNode(head, convertListToListNode(rest));
};

export function deleteDuplicates(head: ListNode | null): ListNode | null {
  const resultValue: number[] = [];

  let currentNode = head;
  if (!currentNode) {
    return head;
  }

  let counter = 0;

  while (currentNode) {
    if (currentNode.val === currentNode.next?.val) {
      counter += 1;
    } else {
      if (counter == 0) resultValue.push(currentNode.val);
      counter = 0;
    }

    currentNode = currentNode?.next ?? null;
  }

  return convertListToListNode(resultValue);
}
