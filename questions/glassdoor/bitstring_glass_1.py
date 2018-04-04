class Node():
    def __init__(self, payload="", parent=None):
        self.payload = payload
        self.parent = parent

    def __str__(self):
        return "{Payload: " + self.payload + " }"


    def __repr__(self):
        return self.__str__()

def push_to_all(nodes, x):
    new_nodes = []
    for node in nodes:
        new_node = Node(node.payload + x, node.parent)
        new_nodes.append(new_node)
    return new_nodes

def split_and_init(nodes):
    new_nodes = []
    for node in nodes:
        left = Node("0", node)
        right = Node("1", node)
        new_nodes.append(left)
        new_nodes.append(right)
    return new_nodes

def get_string(leaf):
    curr = leaf.parent
    result = leaf.payload
    while curr is not None:
        result = curr.payload + result
        curr = curr.parent
    return(result)
    
def main():
    root = Node()
    curr_nodes = []
    curr_nodes.append(root)
    input = input("Enter a bitstring: \n") or "????"

    for x in input:
        if(x == '0' or x == '1'):
            curr_nodes = push_to_all(curr_nodes, x)
        elif(x == '?'):
            curr_nodes = split_and_init(curr_nodes)
        
    for node in curr_nodes:
        print(get_string(node))
