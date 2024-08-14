/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/
class Solution {
    public Node copyRandomList(Node head) {
        Node temp = head;
        Node head2 = new Node(-1);
        Node temp2 = head2;
        if(head == null) return null;
        //create a new list
        while(temp != null){
            Node nn = new Node(temp.val);
            temp2.next = nn;
            temp2 = nn;
            temp = temp.next;
        }
        // 0 -0 -0 -0 - null
        // 0 - currNext -> 0 -0 -0 - null
        head2 = head2.next;
        // make the zigzag
        temp = head;
        temp2 = head2;
        while(temp != null){
            Node currNext = temp2.next;
            temp2.next = temp.next;
            temp.next = temp2;
            temp = temp2.next;
            temp2 = currNext;
        }
        temp = head;
        // temp2 = temp.next;
        // connect the random points
        while(temp != null){
            temp2 = temp.next;
            temp2.random = (temp.random == null) ? null : temp.random.next;
            temp = temp2.next;
            // temp2 = temp.next;
        }
        temp = head;
        temp2 = temp.next;
        // A A' B B' C C'
        // Detachment
        while(temp != null && temp2.next!=null){
            temp.next = temp.next.next;
            temp = temp.next;
            temp2.next = temp2.next.next;
            temp2 = temp2.next;
        }
        temp.next=null;
        return head2;
    }
}
