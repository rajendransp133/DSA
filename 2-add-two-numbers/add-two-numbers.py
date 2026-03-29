# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum_head=ListNode(0,None)
        sum_head_copy=sum_head
        carry=0
        while(l1 or 12):
            if(l1==None and l2==None and carry==0):
                break

            new_node=ListNode(0,None)
            sum_head_copy.next=new_node
            sum_head_copy=sum_head_copy.next

            if(l1 and l2):
                curr_sum=l1.val+l2.val+carry
                l1=l1.next
                l2=l2.next
            elif(l2):
                curr_sum=l2.val+carry
                l2=l2.next
            elif(l1):
                curr_sum=l1.val+carry
                l1=l1.next
            else:
                curr_sum=carry                
            
            if(curr_sum<10):
                sum_head_copy.val=curr_sum
                carry=0
            else:
                sum_head_copy.val=curr_sum%10
                carry=curr_sum//10
        return sum_head.next