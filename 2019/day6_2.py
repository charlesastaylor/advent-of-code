with open('day6.txt') as f:
    map = [line.strip() for line in f]

map = "COM)B B)C C)D D)E E)F B)G G)H D)I E)J J)K K)L K)YOU I)SAN".split()

class Node:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.children = []

    def __str__(self):
        if self.parent:
            return f'Object: {self.name} orbits {self.parent.name} and is directly orbited by {[c.name for c in self.children]}'
        else:
            return f'Object: {self.name} and is directly orbited by {[c.name for c in self.children]}'

    def __repr__(self):
        return self.name

    def print(self, depth=0):
        print(" " * depth + self.name)
        for child in self.children:
            child.print(depth + 1)

    def num_children(self):
        count = 0
        for child in self.children:
            count += 1
            count += child.num_children()
        return count

    def num_orbits(self):
        count = self.num_children()
        for child in self.children:
            count += child.num_orbits()
        return count

    def path_to_com(self):
        path = []
        while self.parent:
            path.append(self.parent)
            self = self.parent
        return path

    def find_node(self, target):
        if self.name == target:
            return self
        for child in self.children:
            ret = child.find_node(target)
            if ret:
                return ret

orbits = {}
for orbit in map:
    parent, child = orbit.split(')')
    orbits.setdefault(parent, []).append(child)

tree = Node('COM', None)
def build_tree(node):
    if node.name in orbits:
        node.children = [Node(name, node) for name in orbits[node.name]]
        for child in node.children:
            build_tree(child)

build_tree(tree)
#tree.print()
#tree.traverse()
#print(tree.path_to_com())
path_you = tree.find_node('YOU').path_to_com()
path_com = tree.find_node('SAN').path_to_com()

for i, obj in enumerate(path_you):
    if obj in path_com:
        print(i + path_com.index(obj))
        break
