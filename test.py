import unittest
from landTree import Node

class LandTreeTestCase(unittest.TestCase):
    def set_up(self):
        # test data structure
        # a; Company a; owner of 6 land parcels ***
        #  | aa; Company aa; owner of 3 land parcels
        #  |  | aaa; Company aaa; owner of 0 land parcels
        #  | ab; Company ab; owner of 0 land parcels
        self.node_a = Node(
            id = 'a',
            name = 'Company a',
            is_root = True
        )
        self.node_a.land = ['l1', 'l2', 'l3']
        
        self.node_aa = Node(
            id = 'aa',
            name = 'Company aa'
        )
        self.node_aa.land = ['l4', 'l5', 'l6']
        self.node_aa.parent = self.node_a
        self.node_a.children.append(self.node_aa)

        self.node_aaa = Node(
            id = 'aaa',
            name = 'Company aaa'
        )
        self.node_aaa.parent = self.node_aa
        self.node_aa.children.append(self.node_aaa)

        self.node_ab = Node(
            id = 'ab',
            name = 'Company ab'
        )
        self.node_ab.parent = self.node_a
        self.node_a.children.append(self.node_ab)

    def test_roots_detected(self):
        self.set_up()
        self.assertTrue(self.node_a.is_root, "Company a should be a root")
        self.assertFalse(self.node_aa.is_root, "Company aa should not be a root")

    def test_get_descendants(self):
        self.set_up()
        self.assertEqual(len(self.node_a.get_descendants()), 3, "Company a should have 3 descendants")
        self.assertEqual(len(self.node_ab.get_descendants()), 0, "Company ab should have 0 descendants")

    def test_get_root(self):
        self.set_up()
        self.assertIs(self.node_aa.get_root(), self.node_a, "Company a should be the root of aa")
        self.assertIs(self.node_aaa.get_root(), self.node_a, "Company a should be the root of aaa")
        self.assertIs(self.node_aaa.get_root(), self.node_aa.get_root(), "Company aa should have the same root as aaa")

    def test_get_level(self):
        self.set_up()
        self.assertEqual(self.node_a.get_level(), 0, "Company a should be level 0")
        self.assertEqual(self.node_aa.get_level(), 1, "Company aa should be level 1")
        self.assertEqual(self.node_aaa.get_level(), 2, "Company aaa should be level 2")

    def test_get_all_land(self):
        self.set_up()
        self.assertEqual(len(self.node_a.get_all_land()), 6, "Company a should have 6 lands in total")
        self.assertIn('l5', self.node_a.get_all_land(), "Company a should own land l5")
        self.assertEqual(len(self.node_aa.get_all_land()), 3, "Company aa should have 3 lands in total")
        self.assertEqual(len(self.node_aaa.get_all_land()), 0, "Company aaa should have 0 lands in total")

    def test_print_node(self):
        self.set_up()
        self.assertEqual(self.node_a.print_node(), 'a; Company a; owner of 6 land parcels')

if __name__ == "__main__":
    unittest.main()
