# my_list = ["apple", "banana", "cherry", "date"]
# # reversed_list = list(reversed(my_list))
# # print(reversed_list)
#
# for i in reversed(my_list):
#     print(i)
#
# smo = ",".join(my_list)
# print(smo)
#
#
# # input size of the list
# n = int(input("Enter the size of list : "))
# # store integers in a list using map,
# # split and strip functions
# lst = list(map(int, input("Enter the integer\
# elements:").strip().split()))[:n]
#
# # printing the list
# print('The list is:', lst)

# lis = [1, 3, 5, 6, 2, 1, 3]
#
# # using sorted() to print the list in sorted order
# print("The list in sorted order is : ")
# for i in sorted(lis):
#     print(i, end=" ")
#
# print("\r")
#
# print(lis)

# print(int(3/2)+1)

# for i in range(2,int(3/2)+1):
#     if i % 2 == 0:
#         print(" in loop",i)
#
# for i in range(2,2):
#     print(i)

# print(2%2)

# # Python3 program to find middle of linked list
# Node class
# class Node:
#
#     # Function to initialise the node object
#     def __init__(self, data):
#         self.data = data  # Assign data
#         self.next = None  # Initialize next as null
#
#
# # Linked List class contains a Node object
# class LinkedList:
#
#     # Function to initialize head
#     def __init__(self):
#         self.head = None
#
#     # Function to insert a new node at the beginning
#     def push(self, new_data):
#         new_node = Node(new_data)
#         new_node.next = self.head
#         self.head = new_node
#
#     # Print the linked list
#     def printList(self):
#         node = self.head
#         while node:
#             print(str(node.data) + "->", end="")
#             node = node.next
#         print("NULL")
#
#     # Function that returns middle.
#     def printMiddle(self):
#         # Initialize two pointers, one will go one step a time (slow), another two at a time (fast)
#         slow = self.head
#         fast = self.head
#
#         # Iterate till fast's next is null (fast reaches end)
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
#
#         # return the slow's data, which would be the middle element.
#         print("The middle element is ", slow.data)
#
#
# # Code execution starts here
# if __name__ == '__main__':
#
#     # Start with the empty list
#     llist = LinkedList()
#
#     for i in range(5, 0, -1):
#         llist.push(i)
#         llist.printList()
#         llist.printMiddle()

# Python program to count the number of time a given
# int occurs in a linked list

# Node class
class Node:

	# Constructor to initialize the node object
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:

	# Function to initialize head
	def __init__(self):
		self.head = None

	# Counts the no . of occurrences of a node
	# (search_for) in a linked list (head)
	def count(self, search_for):
		current = self.head
		count = 0
		while(current is not None):
			if current.data == search_for:
				count += 1
			current = current.next
		return count

	# Function to insert a new node at the beginning
	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	# Utility function to print the LinkedList
	def printList(self):
		temp = self.head
		while(temp):
			print (temp.data)
			temp = temp.next


# Driver program
llist = LinkedList()
llist.push(1)
llist.push(3)
llist.push(1)
llist.push(2)
llist.push(1)

# Check for the count function
print ("count of 1 is % d" %(llist.count(1)))

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)

