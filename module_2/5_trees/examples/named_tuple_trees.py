# type: ignore
from collections import namedtuple


# Node = namedtuple("Node", ["value", "left", "right"])
# tree = Node(
#       value = 1, 
#       left = Node(value = 2, left = None, right = None)), 
#       right = Node(value = 3, left = None, right = None),
# )

# Обход в глубину - dfs
# def process_node(node):
#     if node is None:
#         return
#     process_node_value(node.value)
#     process_node(node.left)
#     process_node(node.right)


from tree import Node, pprint_tree

# print_edges will print all nodes of the tree
def print_edges(node):
    if node == None:
        return
    print(node.value)
    print_edges(node.left)
    print_edges(node.right)

# the same function that uses loops instead
def print_edges_non_recursive(node):
    if node is None:
        return

    stack = [node]
    
    while stack:
        current = stack.pop()
        print(current.value)

        # Push right child first, so left child is processed first
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)    


# count_leaves returns the amount of leaves

def count_leaves(node):
    counter = 0
    if node.left is None and node.right is None:
        counter += 1
    if node.left is not None:
        counter += count_leaves(node.left)
    if node.right is not None: 
        counter += count_leaves(node.right)
    return counter


# get_tree_height returns the depth of the tree

def get_tree_height(node, initial_height=0):
    counter = {"left": initial_height, "right": initial_height}
    if node.left is not None:
        counter['left'] = get_tree_height(node.left, initial_height + 1)
    if node.right is not None:
        counter['right'] = get_tree_height(node.right, initial_height + 1)
    return counter['left'] if counter['left'] >= counter['right'] else counter['right']
    # or you can use return max(counter.values())


def main():
    return

if __name__ == "__main__":
    main()