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
        if node.next:
            node = node.next
    return result

class Solution:
    def addTwoNumbers(self, l1, l2):
        result = []
        currentNodeL1 = l1
        currentNodeL2 = l2
        carry = 0

        while currentNodeL1 or currentNodeL2:
            if not currentNodeL1 is None and not currentNodeL2 is None:
              sum = currentNodeL1.val + currentNodeL2.val + carry
              currentNodeL1 = currentNodeL1.next
              currentNodeL2 = currentNodeL2.next
            elif currentNodeL2 is None:
              sum = currentNodeL1.val + carry
              currentNodeL1 = currentNodeL1.next
            elif currentNodeL1 is None:
              sum = currentNodeL2.val + carry
              currentNodeL2 = currentNodeL2.next
                
            carry = 1 if sum >= 10 else 0
            low = sum % 10
            result.append(low)
        
        if carry == 1:
           result.append(1)

        return convertArrayToListNode(result)