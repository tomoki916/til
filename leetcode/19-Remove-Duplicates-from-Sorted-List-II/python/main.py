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


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummyHead = ListNode(0, head)
        prev = dummyHead
        currentNode = head

        while not currentNode == None:
            while not currentNode.next == None and currentNode.val == currentNode.next.val:
                currentNode = currentNode.next

            if not prev.next == currentNode:
                # 重複がある場合、prevからcurrentNodeまでを削除する
                prev.next = currentNode.next
            else:
                # 重複がない場合、次の比較のために基準点を今のノードにする
                prev = currentNode

            currentNode = currentNode.next

        return dummyHead.next
