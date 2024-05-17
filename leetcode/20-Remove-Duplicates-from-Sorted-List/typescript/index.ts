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

export const convertListToListNode = (l: number[]): ListNode => {
  const head = l[0];
  if (l.length === 1) return new ListNode(head, null);
  const rest = l.slice(1);
  return new ListNode(head, convertListToListNode(rest));
};

export function deleteDuplicates(head: ListNode | null): ListNode | null {
  if (!head) return null;
  if (!head.next) return head;

  let prev = head;
  let current: ListNode | null = head.next;

  while (current) {
    while (current && current.val === prev.val) {
      current = current.next;
    }

    prev.next = current;
    prev = current as ListNode;

    if (current) current = current.next;
  }

  return head;
}
