class Node():
	def __init__(self, payload="", left=None, right=None):
		self.payload = payload
		self.left = left
		self.right = right
	
	def __str__(self):
		return "{Payload: " + self.payload + " Left: " + str(self.left) + " Right: " + str(self.right) + "}"
		
		
	def __repr__(self):
		return self.__str__()
		
def push_to_all(nodes, x):
	for node in nodes:
		node.payload = node.payload + x
		
def split_and_init(nodes):	
	for node in nodes:
		left = Node("0", None, None)
		right = Node("1", None, None)
		new = Node(node.payload, left, right)
		nodes.remove(node)
		nodes.append(new)
		
def advance(nodes):
	
	##Need to create new list to mutate
	print("Before: ")
	print(nodes)
	print("\n")
	for node in nodes:
		print("My node: " + str(node))
		left = node.left
		right = node.right
		nodes.remove(node)
		nodes.append(left)
		nodes.append(right)
		
	print("After: ")
	print(nodes)
	print("\n")
	
def print_string(root, prev_payload):
	new_payload = prev_payload + root.payload
	if root.left is not None and root.right is not None:
		print_string(root.left, new_payload)
		print_string(root.right, new_payload)
	else:
		print(new_payload)
		
root = Node()
curr_nodes = []
curr_nodes.append(root)
input = "0?1"
#input = input("Enter a bitstring: \n") or "0?1"

for x in input:
	if(x == '0' or x == '1'):
		push_to_all(curr_nodes, x)
	elif(x == '?'):
		split_and_init(curr_nodes)
		advance(curr_nodes)

print_string(root, root.payload)

