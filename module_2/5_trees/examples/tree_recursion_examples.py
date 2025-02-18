def traverse_tree(tree, depth=0):
    for node, children in tree.items():
        print("  " * depth + node)  # Indent based on depth
        traverse_tree(children, depth + 1)  # Recur on children


def count_nodes(tree):
    count = 0
    for node, children in tree.items():
        count += 1 # count this node
        count += count_nodes(children) # recursively count child nodes
    return count


def search_node(tree, target):
    for node, children in tree.items():
        if node == target:
            return True
        if search_node(children, target):
            return True
    return False


def insert_node(tree, parent, new_node):
    if parent in tree:
        tree[parent][new_node] = {} # add new node
        return True
    for node, children in tree.items():
        if insert_node(children, parent, new_node): # recur on child nodes
            return True
    return False


def main():
    tree1 = {
    "root": {
        "A": {
            "A1": {},
            "A2": {
                "A2a": {}
                }
            },
        "B": {
            "B1": {}
            }
        }
    }

    traverse_tree(tree1)
    print(count_nodes(tree1))
    print(search_node(tree1, "A2a"))
    print(search_node(tree1, "C")) 
    insert_node(tree1, "A2", "A2b")
    traverse_tree(tree1)
    return

if __name__ == "__main__":
    main()