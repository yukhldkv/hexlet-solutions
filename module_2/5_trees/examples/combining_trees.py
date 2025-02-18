def merge_dicts(a, b):  
    for key, value1 in b.items():
        value2 = a.get(key, [])
        a[key] = list(set(value1 + value2))
    return a


def build_neighbors(branch):
    neighbors_from_branch = {}
    def _dfs(tree, parent = None):
        if len(tree) == 1:
            node = tree[0]
            neighbors_from_branch[node] = [parent]
            return node
        node, neighbors = tree
        neighbors_from_branch[node] = []
        if parent:
            neighbors_from_branch[node].append(parent)
        for neighbor in neighbors:
            child = _dfs(neighbor, node)
            neighbors_from_branch[node].append(child)
        return node

    _dfs(branch)
    return neighbors_from_branch


def build_tree(root, neighbors):
    used_nodes = set()
    def _build(node):
        used_nodes.add(node)
        trees = []
        for neighbor in neighbors[node]:
            if neighbor not in used_nodes:
                tree = _build(neighbor)
                if tree:
                    trees.append([neighbor, tree])
                else:
                    trees.append([neighbor])
        return trees
    tree = [root, _build(root)]
    return tree


def combine(*branches):
    root = branches[0][0]

    neighbors = {}
    for branch in branches:
        neighbors = merge_dicts(neighbors, build_neighbors(branch))
    

    tree = build_tree(root, neighbors)
    return tree


def main():
    branch1 = ['A', [         #   A
        ['B', [               #   |
            ['C'],            #   B
            ['D'],            #  / \
        ]],                   # C   D
    ]]

    branch2 = ['B', [         #   B
        ['D', [               #   |
            ['E'],            #   D
            ['F'],            #  / \
        ]],                   # E   F
    ]]

    branch3 = ['I', [         #   I
        ['A', [               #   |
            ['B', [           #   A
                ['C'],        #   |
                ['H'],        #   B
            ]],               #  / \
        ]],                   # C   H
    ]]
    #print(build_neighbors(branch1))
    print(combine(branch1, branch2, branch3))
    return

if __name__ == "__main__":
    main()