class TreeError(Exception):
    pass


class TreeNode:
    def __init__(self, tree, value=None, children=None, is_root=False):
        self.tree = tree
        if children is None:
            self.children = []
        else:
            self.children = children
        if len(children) != len(set(children)):
            raise TreeError(
                "list of children can't contain duplicates!"
                )
        for child in children:
            if child.is_root:
                raise TreeError(
                    "root can't be a child!"
                    )
        self.value = value
        self.is_root = is_root
        
    def __repr__(self):
        return "TreeNode with value {}".format(self.value)
    
    
class Tree:
    def __init__(self, root_value=None):
        self.root = TreeNode(self, value=root_value, is_root=True)
            
        
    
    