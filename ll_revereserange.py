# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @param C : integer
    # @return the head node in the linked list
    def reverseBetween(self, A, B, C):
        # If the linked list is empty or has only one node, return the list as is
        if A == None or A.next == None:
            return A

        # Initialize pointers and counters
        prev = None
        x = A
        i = 1

        # Traverse the linked list until we reach the B-th node
        while i < B:
            prev = x
            x = x.next
            i += 1

        # Store the B-th node and the node before it (if it exists)
        N0 = prev
        N1 = x

        # Reverse the sublist between B and C
        prev = None
        while i <= C:
            temp = x.next
            x.next = prev
            prev = x
            x = temp
            i += 1

        # Connect the reversed sublist to the original list
        N1.next = x
        if N0:
            N0.next = prev
            return A
        else:
            return prev