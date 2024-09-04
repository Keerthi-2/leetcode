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
    public ListNode mergeKLists(ListNode[] lists) {
        // ListNode head=null;



List<Integer> ans=new ArrayList<>();

for(int i=0; i<lists.length; i++){

ListNode curr=lists[i]; ///[1,4,5]

while(curr!=null){

ans.add(curr.val); //[1,4,5]

curr=curr.next;

}

}



Collections.sort(ans);

System.out.print(ans);
ListNode n=new ListNode(-1);

ListNode t=n;
        
for(int i=0; i<ans.size(); i++){


ListNode nen=new ListNode(ans.get(i));
    
    
n.next=nen;

n=n.next;

}

return t.next;
    }
}