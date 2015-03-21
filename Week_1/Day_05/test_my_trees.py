import unittest

import my_trees


class TreeTest(unittest.TestCase):
    def test_create_empty_tree(self):
        my_tree = my_trees.Tree()
        self.assertEqual(my_tree.root, None)
        self.assertEqual(my_tree.nodes, set([]))
        
    def test_create_tree_with_one_valueless_node(self):
        my_node = my_trees.TreeNode()
        my_tree = my_trees.Tree(root=my_node)
        self.assertEqual(my_node.children, [])
        self.assertEqual(my_tree.root, my_node)
        self.assertEqual(my_tree.nodes, set([my_node]))
        
    def test_create_tree_with_one_valued_node(self):
        my_node = my_trees.TreeNode(value=2)
        my_tree = my_trees.Tree(root=my_node)
        self.assertEqual(my_node.__repr__(), "TreeNode with value 2")
        self.assertEqual(str(my_node), "TreeNode with value 2")
        self.assertEqual(my_node.children, [])
        self.assertEqual(my_tree.root, my_node)
        self.assertEqual(my_tree.nodes, set([my_node]))  
        
    def test_can_add_node(self):
        my_tree = my_trees.Tree()
        root = my_tree.add_node(value=0)
        node_1 = my_tree.add_node(parent=root, value=1)
        node_2 = my_tree.add_node(parent=root, value=2)
        node_3 = my_tree.add_node(parent=node_1, value=3)
        node_4 = my_tree.add_node(parent=node_1, value=4)
        node_5 = my_tree.add_node(parent=node_2, value=5)
        node_6 = my_tree.add_node(parent=node_2, value=6)
        self.assertEqual(my_tree.nodes, set([root, node_1, node_2, node_3,
        node_4, node_5, node_6]))
        
    def test_root_node_has_two_children(self):
        pass
    
    def test_DFS_can_find_node(self):
        node_1 = my_trees.TreeNode(value=1)
        my_tree = my_trees.Tree(root=node_1)
        # node_2 = my_trees.add_node(parent)
    
    def test_BFS_can_find_node(self):
        pass
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    



if __name__ == '__main__':
    unittest.main()