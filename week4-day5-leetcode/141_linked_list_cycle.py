# https://leetcode.com/problems/linked-list-cycle/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head # None

        # loop: number of times known     
        # while: NO
        # for: YES
        while fast != None and fast.next != None: # to avoid None.next
            slow = slow.next # 1 node
            fast = fast.next.next # 2 nodes

            if fast == slow:
                return True
        
        return False


        # fast = head
        #loop:
            # if fast.next == None:
            #     return False
            # if fast.next.next:
            #     return True
            # fast = fast.next
 
# Time Complexity: O(n)
# Space Complexity: O(1)