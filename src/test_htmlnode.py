import unittest

from htmlnode import HTMLNode 


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("a", "tester", None, {"href": "https://www.google.com","target": "_blank",})
        to_html = node.props_to_html()
        self.assertEqual(to_html, "href=\"https://www.google.com\" target=\"_blank\"")           
    def test_repr(self):
        node = HTMLNode("a", "tester", None, {"href": "https://www.google.com","target": "_blank",})
        self.assertNotEqual(node.__repr__(), "HTMLNode(\"a\", \"tester\", None, {\"href\": \"https://www.google.com\",\"target\": \"_blank\",})")         

    def test_props_to_html(self):
        node = HTMLNode("a", "tester", None, None)
        to_html = node.props_to_html()
        self.assertEqual(to_html, "")

if __name__ == "__main__":
    unittest.main()
