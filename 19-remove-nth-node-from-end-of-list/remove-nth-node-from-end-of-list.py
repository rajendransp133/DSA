# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count=0
        node=head
        while(node!=None):
            count+=1
            node=node.next
        index_from_front=count-n
        if(index_from_front==0):
            return head.next
        count=0
        node=head
        while(node!=None):
            count+=1
            if(count==index_from_front):
                if(node.next.next!=None):
                    node.next=node.next.next
                else:
                    node.next=None
                break
            node=node.next
        return head
                
            


