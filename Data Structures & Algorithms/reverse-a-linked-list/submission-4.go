/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func reverseList(head *ListNode) *ListNode {
    // if not head{
	// 	return nil
	// }
	var prev *ListNode = nil
	var curr *ListNode = head

	for curr != nil {
		var temp *ListNode = curr.Next
		curr.Next = prev
		prev = curr
		curr = temp
	}

	return prev
}
