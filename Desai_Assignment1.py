#Implementation of Queue
import Queue

q = Queue.Queue()
print "Queue:"
for i in range(10):
	q.put(i)
	
while not q.empty():
	print q.get()

print "____________________________________________"
#Implementation of Stack

class stack:
	def __init__(self):
		self.data = []
	
	def push(self, integer):
		self.data.append(integer)
	
	def pop(self):
		return self.data.pop()
	
	def checkSize(self):
		return len(self.data)
		
s = stack()
 
print "The current size of the stack is:"
print (s.checkSize())
print "\n"

for j in range(10):
	s.push(j)
print "The current size of the stack after pushing 10 integers to the stack is:"
print (s.checkSize())
print "\n"

print "Stack:"
for i in range(10):
	print s.pop()
print "\n"
print "The current size of the stack after popping 10 integers from the stack is:"
print (s.checkSize())

print "___________________________________________________________"



#Implementation for Binary Tree

#Creating a Node for the Binary Tree



class Node:
    def __init__(self, iKey):
        self.key = iKey
        self.lChild = None
        self.rChild = None
        self.pKey = None

class Tree:
	def __init__(self, iKey):
		self.key = iKey
		self.lChild = None
		self.rChild = None
		self.pKey = None
	
	def delete(self, iKey, rootNode):
		if rootNode is None:
			print "Node not found"
			return False
		elif iKey == rootNode.key:
			if rootNode.lChild or rootNode.rChild:
				print "Node not deleted: has children"
				return False
			else:
				del rootNode.lChild
				del rootNode.rChild
				del rootNode.pKey
				del rootNode.key
				del rootNode
				return True
		elif iKey < rootNode.key:
			self.delete(iKey,rootNode.lChild)
		else:
			try:
				self.delete(iKey,rootNode.rChild)
			except:
				pass

def add(parentValue,value):
	if parentValue is None:
		print "Parent not found"
	else:
		if parentValue.key > value.key:
			if parentValue.lChild == None:
				parentValue.lChild = value
				value.pKey = parentValue
			else:
				add(parentValue.lChild, value)
		else:
			if parentValue.rChild == None:
				parentValue.rChild = value
				value.pKey = parentValue
			else:
				add(parentValue.rChild,value)
				
def printTree(rootNode):
	if not rootNode:
		return
	try:
		print rootNode.key
	except:
		pass
	try:
		printTree(rootNode.lChild)
	except:
		pass
	try:
		printTree(rootNode.rChild)
	except:
		pass
print "Binary Tree:\n"					
print "Inputing integers from 0-9 in order \n"
BT = Tree(0)
add(BT,Node(1))
add(BT,Node(2))
add(BT,Node(3))
add(BT,Node(4))
add(BT,Node(5))
add(BT,Node(6))
add(BT,Node(7))
add(BT,Node(8))
add(BT,Node(9))

print "The preorder traversal is: \n"

printTree(BT)
print "\n"

print "Deleting 8:"

BT.delete(8,BT)

print "Deleting 9:"
BT.delete(9,BT)

printTree(BT)


print "____________________________________________________________________"


#Implementation of a Graph

print "Graph:\n"
class Graph():
	def __init__(self):
		self.vertexList = {}
	def addVertex(self, value):
		if (value in self.vertexList):
			print "Vertex already exists"
		else:
			self.vertexList[value] = []
		return
		
	def addEdge(self, value1, value2):
		if value1 not in self.vertexList:
			print ("One or more vertices not found")
		elif value2 not in self.vertexList:
			print ("One or more vertices not found")
		else:
			self.vertexList[value1].append(value2)
			self.vertexList[value2].append(value1)
		return
	
	def findVertex(self,value):
		if (value not in self.vertexList):
			print "Vertex doesn't exist."
		else:
			print str(value) + ' ' +"has adjacency list" + ' ' + str(self.vertexList[value])
		return
		
		
		
	
g = Graph()

print "Create 10 integers as vertices"
for i in range (5,15):
	g.addVertex(i)
print " Complete \n"
print "Adding an existing vertex: 5"	
g.addVertex(5)
print "\n"

print "Add 20 edges" 
g.addEdge(5, 5)
g.addEdge(5, 6)
g.addEdge(5, 12)
g.addEdge(6, 6)
g.addEdge(6, 8)
g.addEdge(6, 12)
g.addEdge(8, 14)
g.addEdge(8, 6)
g.addEdge(8, 9)
g.addEdge(10, 11)
g.addEdge(14, 12)
g.addEdge(6, 8)
g.addEdge(9, 5)
g.addEdge(10, 11)
g.addEdge(10, 12)
g.addEdge(10, 13)
g.addEdge(7, 11)
g.addEdge(11, 14)
g.addEdge(13, 13)
g.addEdge(8, 13)
print "Complete \n"


print "Find the adjacency lists for 5 vertices: 5,8,12,14,10\n"
g.findVertex(5)
g.findVertex(8)
g.findVertex(12)
g.findVertex(14)
g.findVertex(10)
print "Complete\n"
