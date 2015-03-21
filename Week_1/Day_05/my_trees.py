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
            return new_node
        elif self.root:
            parent = self.root
            new_node = TreeNode(value, children, is_root)
            parent.add_child(new_node)
            self.nodes.add(new_node)
            return new_node            
        else:
            self.root = TreeNode(value, children, is_root=True)
            self.nodes = set([self.root])
            return self.root
            
    def delete_node(self, node):
        descendants = self.get_descendants_DFS(node)                
        assert set(descendants) == set(self.get_descendants_BFS(node))
        for descendant in descendants:
            self.nodes.remove(descendant)
            del descendant.children
            
    def get_descendants_DFS(self, node):
        descendants = []
        stack = [node]
        while stack:
            v = stack.pop()
            descendants.append(v)
            for child in v.children:
                stack.append(child)
        return descendants
        
    def get_descendants_BFS(self, node):
        descendants = []
        queue = deque([node])
        while queue:
            v = queue.popleft()
            descendants.append(v)
            for child in v.children:
                queue.append(child)
        return descendants
            
    def contains_DFS(self, node):
        if self.root:
            stack = [self.root]
            while stack:
                v = stack.pop()
                if v != node:
                    for child in v.children:
                        stack.append(child)
                else:
                    return True
            return False
        else:
            return False
        
    
    def contains_BFS(self, node):
        if self.root:
            queue = deque([self.root])
            while queue:
                v = queue.popleft()
                if v != node:
                    for child in v.children:
                        queue.append(child)
                else:
                    return True
            return False
        else:
            return False
        
        

    

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
                    
    def remove(self):
        pass
        
        
    

class TreeError(Exception):
    pass          
            
        
    
    