class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def convertArrayToListNode(nums):
    if len(nums) == 1:
        return ListNode(nums[0])
    return ListNode(nums[0], convertArrayToListNode(nums[1:]))


def convertListNodeToArray(nodes):
    result = []
    node = nodes
    while node:
        result.append(node.val)
        node = node.next
    return result
