class Node():
	def __init__(self, payload=None, left=None, right=None):
		self.payload = payload
		self.left = left
		self.right = right


l1 = Node(5)
l2 = Node(4, l1)
l3 = Node(3, l2)
l4 = Node(2, l3)

m1 = Node(1, l4)
m2 = Node(0, m1)

r = Node(-1, m2)

def get_next_candidates(nodes):
	next = []
	for node in nodes:
		if node.left is not None:
			next.append(node.left)
		if node.right is not None:
			next.append(node.right)
	return next

def height(root):
	candidates = [root]
	counter = 0
	while len(candidates) > 0:
		candidates = get_next_candidates(candidates)
		counter += 1
	return counter
	
print(height(r))
