class TreeError(Exception):
    pass


class TreeNode:
    def __init__(self, tree, value=None, children=None, is_root=False):
        self.tree = tree
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
        
        
    
class Tree:
    def __init__(self, root_value=None):
        self.root = TreeNode(self, value=root_value, is_root=True)
        
    def add_node(
        self, parent=self.root, value=None, children=None, is_root=False
        ):
        parent.add_child(TreeNode(self, value, chidren, is_root))
        
            
        
    
    