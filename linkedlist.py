# -*- coding: utf-8 -*-
import unittest

class Node:
	"""
		Implement a class Node that will be used as base unit for the singly linked list implementation
	"""
	def __init__(self,key):
		"""
			The constructor

			:param key: key to store in the Node object
			:type key: int,str
			:attr key: key to store in the Node object
			:attr next: point to the next node reference in the list
			:type next: obj<Node> (Default: None)
		"""
		self.key = key
		self.next = None

class LinkedList:
	"""
		Implement a basic singly unordered linked list
	"""
	def __init__(self,head=None):
		"""
			The constructor

			:param head: Node used as head (Default: None) 
			:type head: obj<Node>
		"""
		self.head = None

	def insert(self,key):
		"""
			Insert a key at the head of the list

			:param key: The key to insert
			:type key: int, string
			:return: None 
		"""
		new_node = Node(key)
		new_node.next = self.head
		self.head = new_node

	def search(self,key):
		"""
			Search for a key in the linked list.

			:param key: The key to search
			:type key: int, string
			:return: Return the Node containing the key if found
			:rtype: obj<Node> 
		"""
		curentNode = self.head
		key_found = False
		while curentNode and not key_found:
			if curentNode.key == key:
				key_found = True
			else:
				curentNode = curentNode.next
		if not curentNode:
			raise KeyError("Key not found")
		return curentNode

	def size(self):
		"""
			Compute the number of nodes contained in the list

			:return: The lenght of list
			:rtype: int
		"""
		curentNode = self.head
		counter = 0
		while curentNode:
			counter += 1
			curentNode = curentNode.next
		return counter

	def delete(self, key):
		curentNode = self.head
		previousNode = None
		while curentNode:
			if curentNode.key == key:
				if previousNode:
					previousNode.next =  curentNode.next
					return curentNode
				else:
					self.head = curentNode.next
					return curentNode

			previousNode = curentNode
			curentNode = curentNode.next


class TestLinkedList(unittest.TestCase):

	def testInsert(self):
		li = LinkedList()
		li.insert(3)
		self.assertTrue(li.head.key == 3)
		li.insert("antoine")
		self.assertTrue(li.head.key == "antoine")
		self.assertTrue(li.head.next.key == 3)


	def testDelete(self):
		li = LinkedList()
		li.insert(3)
		self.assertTrue(li.delete(3).key == 3)
		li.insert(3)
		li.insert(7)
		li.insert("abc")
		li.insert("z")
		self.assertTrue(li.delete("abc").key == "abc")
		self.assertTrue(li.size() == 3)


	def testSearch(self):
		li = LinkedList()
		li.insert(3)
		li.insert(-345)
		li.insert("abc")
		li.insert("zz")
		self.assertTrue(li.search("abc").key == "abc" )

	def testSize(self):
		li = LinkedList()
		li.insert(3)
		li.insert("abc")
		li.insert(-345)
		self.assertTrue(li.size() == 3)

if __name__ == "__main__":
	unittest.main()



