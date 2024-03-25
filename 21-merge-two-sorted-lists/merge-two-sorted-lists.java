/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {

public ListNode mergeTwoLists(ListNode list1, ListNode list2) {

if(list1==null)
return list2;
if(list2==null)
return list1;
ListNode curr = null ;

ListNode head = null ;

ListNode Ahead = list1 ;

ListNode Bhead = list2 ;

if ( (Ahead.val <= Bhead.val) )

{

head = Ahead ;

curr = Ahead ;

Ahead = Ahead.next ;

}

else

{

head = Bhead ;

curr = Bhead ;

Bhead = Bhead.next ;

}

while ( Ahead!= null && Bhead != null)

{

if ((Ahead.val <= Bhead.val))

{

curr.next = Ahead ;

curr = Ahead ;

Ahead = Ahead.next ;

}

else

{

curr.next = Bhead ;

curr = Bhead ;

Bhead = Bhead.next ;

}

}
if(Ahead!=null){
    curr.next=Ahead;
}
if(Bhead!=null){
    curr.next=Bhead;
}
return head;

}

}