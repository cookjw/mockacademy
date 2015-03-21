from collections import deque

class Tree:
            
    def __init__(self, root=None):
        self.root = root
        if self.root is not None:            
            self.nodes = set([self.root])
            self.root.is_root = True
        else:
            self.nodes = set([])            
        
    def add_node(
        self, parent=None, value=None, children=None, is_root=False
        ):
        if parent:
            new_node = TreeNode(value, children, is_root)
            parent.add_child(new_node)
            self.nodes.add(new_node)
            self.check_binary()
            return new_node
        elif self.root:
            parent = self.root
            new_node = TreeNode(value, children, is_root)
            parent.add_child(new_node)
            self.nodes.add(new_node)
            self.check_binary()
            return new_node            
        else:
            self.root = TreeNode(value, children, is_root=True)
            self.nodes = set([self.root])
            self.check_binary()
            return self.root
        
            
    def delete_node(self, node):
        descendants = self.get_descendants_DFS(node)                
        assert set(descendants) == set(self.get_descendants_BFS(node))
        for descendant in descendants:
            self.nodes.remove(descendant)
            del descendant.children
            
    def move_node(self, node, new_parent, position=None):
        if node in self.nodes and not node.is_root:
            parent = [x for x in self.nodes if node in x.children][0]
            parent.children.remove(node)
            if position is None:
                new_parent.children.append(node)
            else:
                children = new_parent.children
                new_parent.children = children[:position] + [node] + \
                    children[position:]
        elif node.is_root:
            raise TreeError("Can't move root node!")
        else:
            raise TreeError("Node not in tree.")
        self.check_binary()
            
                        
            
    def get_descendants_DFS(self, node):
        if node in self.nodes:
            descendants = []
            stack = [node]
            while stack:
                v = stack.pop()
                descendants.append(v)
                for child in v.children:
                    stack.append(child)
            return descendants
        else:
            raise TreeError("Node not in tree.")
        
    def get_descendants_BFS(self, node):
        if node in self.nodes:
            descendants = []
            queue = deque([node])
            while queue:
                v = queue.popleft()
                descendants.append(v)
                for child in v.children:
                    queue.append(child)
            return descendants
        else:
            raise TreeError("Node not in tree.")
            
    def contains_DFS(self, node):    
        nodes = self.get_descendants_DFS(self.root)
        return node in nodes        
    
    def contains_BFS(self, node):
        nodes = self.get_descendants_BFS(self.root)
        return node in nodes    
        
    def check_binary(self):
        if isinstance(self, BinaryTree):
            self.binary_check()
            

   
class BinaryTree(Tree):
    
    def __init__(self):
        Tree.__init__(self)
        self.binary_check()
        
    def binary_check(self):
        for node in self.nodes:
            if len(node.children) <= 2:
                pass
            else:
                raise TreeError(
                "Binary tree node has more than two children."
                )
        
   
   
   
class TreeNode:
    
    def __init__(self, value=None, children=None, is_root=False):        
        if children is None:
            self.children = []
        else:
            self.children = children
        self.value = value
        self.is_root = is_root
        
    def __repr__(self):
        return "TreeNode with value {}".format(self.value)
        
    def add_child(self, node):
        self.children.append(node)
        self.check_children()
        
    def check_children(self):
        children = self.children
        if len(children) != len(set(children)):
            raise TreeError(
                "list of children can't contain duplicates!"
                )
        for child in children:
            if child.is_root:
                raise TreeError(
                    "root can't be a child!"
                    )        
                    
class TreeError(Exception):
    pass          
            
        
    
    