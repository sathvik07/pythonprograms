import math

def ncr(n,r):
    res = 1

    for i in range(r):
        res = res * (n - i)
        res = res // (i + 1)
    return res


def pascaltriangle(r,c):
    elem = ncr(r-1, c-1)
    return elem

print(pascaltriangle(5,3))





# Definition for singly-linked list.
class ListNode:
   def __init__(self, x):
       self.val = x
       self.next = None

class Solution:
    # @param A : head node of linked list
    # @return an integer
    def solve(self, A):
        slow = A
        fast = A
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow.val

