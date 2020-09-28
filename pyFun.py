# print("Enter a name: ")
# name = input()
# print("Hi,",name)
#
# print("How hot are you: ")
# hot_lvl = input()
# hot_lvl = int(hot_lvl)
# if hot_lvl < 1:
# 	print("I am so sorry")
# elif hot_lvl >= 1 and hot_lvl <= 3:
# 	print("You kind of ugly I guess")
# else:
# 	print("You HOT af papi")
#
#
# str = ''
# while str != 'penis':
# 	print("Enter penis, pls")
# 	str = input()
# print("Thanks, bitch")


# import random
# num = -1
# counts = 0
# avg = 0
#
# while num != 69:
# 	# print(num)
# 	num = random.randint(1,1000)
# 	counts += 1
# print("That took: " + str(counts) + " iterations")
class Node:
	# def __init__(self, weight, left, right):
	def __init__(self, weight):
		self.weight = weight
		self.next = None
		# self.left = None
		# self.right = None
class LinkedList:
	def __init__(self):
		self.head = None

	def insert_at_head(weight):
		new_node = Node(weight)
		new_node.next = self.head
		self.head = new_node

	def print_list(self):
		print_node = self.head
		while print_node is not None:
			print(print_node.weight)
			print_node = print_node.next


list = LinkedList()
list.head = Node(2)
node1 = Node(24)
node2 = Node(4)
node3 = Node(69)
list.head.next = node1
node1.next = node2
node2.next = node3

list.print_list()
