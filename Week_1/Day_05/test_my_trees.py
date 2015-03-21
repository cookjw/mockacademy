import unittest

import my_trees

def construct_tree():
    global my_tree, root, node_1, node_2, node_3, node_4, node_5, node_6    
    my_tree = my_trees.Tree()
    root = my_tree.add_node(value=0)
    node_1 = my_tree.add_node(parent=root, value=1)
    node_2 = my_tree.add_node(parent=root, value=2)
    node_3 = my_tree.add_node(parent=node_1, value=3)
    node_4 = my_tree.add_node(parent=node_1, value=4)
    node_5 = my_tree.add_node(parent=node_2, value=5)
    node_6 = my_tree.add_node(parent=node_2, value=6)    

construct_tree() 

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
        self.assertEqual(my_tree.nodes, set([root, node_1, node_2, node_3,
        node_4, node_5, node_6]))
        self.assertEqual(root.children, [node_1, node_2])
        self.assertEqual(node_1.children, [node_3, node_4])
        self.assertEqual(node_2.children, [node_5, node_6]) 

    def test_can_delete_node(self):         
        self.assertIn(node_6, my_tree.nodes)        
        my_tree.delete_node(node_6)
        self.assertNotIn(node_6, my_tree.nodes)        
        construct_tree() 
        self.assertIn(node_6, my_tree.nodes)
        my_tree.delete_node(node_2)
        self.assertNotIn(node_2, my_tree.nodes)
        self.assertNotIn(node_6, my_tree.nodes) 
        construct_tree()        

    
    def test_DFS_can_find_node(self):        
        for node in my_tree.nodes:
            self.assertTrue(my_tree.contains_DFS(node))

    def test_DFS_cannot_find_absent_node(self):        
        self.assertFalse(my_tree.contains_DFS(my_trees.TreeNode(value=100)))    
    
    def test_BFS_can_find_node(self):        
        for node in my_tree.nodes:
            self.assertTrue(my_tree.contains_BFS(node))
            
    def test_BFS_cannot_find_absent_node(self):        
        self.assertFalse(my_tree.contains_BFS(my_trees.TreeNode(value=100)))    

    def test_can_get_subtree_DFS(self):
        self.assertEqual(set(my_tree.get_descendants_DFS(root)), my_tree.nodes)
        
    def test_can_get_subtree_BFS(self):
        self.assertEqual(set(my_tree.get_descendants_BFS(root)), my_tree.nodes)
        
    def test_construct_tree(self):
        self.assertEqual(len(my_tree.nodes), 7)
        
                
    
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    



if __name__ == '__main__':
    unittest.main()