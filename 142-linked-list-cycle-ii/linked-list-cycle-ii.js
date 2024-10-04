/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var detectCycle = function(head) {
  
        if (head === null || head.next === null) {
            // If there is no loop (pos = 0) or the list is empty/has one node, return as is
            return null;
        }
        //find loop in LL
        let slow = head;
        let fast = head;
        let isCycle = false;
        while(fast.next != null && fast.next.next != null){
            slow = slow.next;
            fast = fast.next.next;
            if(slow == fast){
                isCycle = true;
                break;
            }
        }
        //If no loop in LL return -1
        if(isCycle == false){
            return null;
        }
        //Break the loop by finding the metting point from middle and other one from head
        let i = head;
        let j = slow;
        while(i !== j){
            i = i.next;
            j = j.next;
        }
    return i;
      
        // return i;
    
};