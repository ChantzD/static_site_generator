import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.LINK)
        self.assertNotEqual(node, node2)           

    def test_not_eq_w_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "www.test.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "www.test2.com")
        self.assertNotEqual(node, node2)         

    def test_eq_w_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "www.test.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "www.test.com")
        self.assertEqual(node, node2)    

if __name__ == "__main__":
    unittest.main()
