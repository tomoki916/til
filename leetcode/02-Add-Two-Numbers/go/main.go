package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func convertToListNodeFromList(l []int) *ListNode {
	if len(l) == 1 {
		node := &ListNode{l[0], nil}
		return node
	}
	nodes := &ListNode{l[0], convertToListNodeFromList(l[1:])}
	return nodes
}

func convertToListFromNodeList(nodes *ListNode) []int {
	resultList := []int{}
	currentNode := nodes

	for currentNode != nil {
		resultList = append(resultList, currentNode.Val)
		currentNode = currentNode.Next
	}

	return resultList
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	currentL1Node := l1
	currentL2Node := l2
	carry := 0
	tmpSum := 0
	resultList := []int{}

	for {
		if currentL1Node != nil && currentL2Node != nil {
			tmpSum = currentL1Node.Val + currentL2Node.Val + carry
			currentL1Node = currentL1Node.Next
			currentL2Node = currentL2Node.Next
		} else if currentL1Node != nil {
			tmpSum = currentL1Node.Val + carry
			currentL1Node = currentL1Node.Next
		} else if currentL2Node != nil {
			tmpSum = currentL2Node.Val + carry
			currentL2Node = currentL2Node.Next
		} else {
			break
		}

		if tmpSum >= 10 {
			carry = 1
		} else {
			carry = 0
		}
		resultList = append(resultList, tmpSum%10)
	}

	if carry > 0 {
		resultList = append(resultList, 1)
	}

	return convertToListNodeFromList(resultList)
}
