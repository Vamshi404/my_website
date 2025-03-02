import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_no_props(self):
        node = HTMLNode(tag="p", value="This is a paragraph.")
        self.assertEqual(node.props_to_html(), "")
        self.assertEqual(repr(node), "HTMLNode(tag=p, value=This is a paragraph., children=[], props={})")

    def test_with_props(self):
        props = {"href": "https://www.google.com", "target": "_blank"}
        node = HTMLNode(tag="a", value="Click Here", props=props)
        self.assertEqual(node.props_to_html(), 'href="https://www.google.com" target="_blank"')
        self.assertEqual(repr(node), 'HTMLNode(tag=a, value=Click Here, children=[], props={\'href\': \'https://www.google.com\', \'target\': \'_blank\'})')

    def test_with_children(self):
        child_node = HTMLNode(tag="span", value="This is a child")
        parent_node = HTMLNode(tag="div", children=[child_node])
        self.assertEqual(len(parent_node.children), 1)
        self.assertEqual(parent_node.children[0].value, "This is a child")
        self.assertEqual(repr(parent_node), "HTMLNode(tag=div, value=None, children=[HTMLNode(tag=span, value=This is a child, children=[], props={})], props={})")

if __name__ == "__main__":
    unittest.main()
