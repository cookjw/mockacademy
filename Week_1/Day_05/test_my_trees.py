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
        
    def test_root_node_has_two_children(self):
        pass
    
    def test_DFS_can_find_node(self):
        pass
    
    def test_BFS_can_find_node(self):
        pass
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    



if __name__ == '__main__':
    unittest.main()