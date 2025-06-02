""" class HTMLNode():
    def __init__(self, tag=None, value str | None=None, children: HTMLNode | None=None, props: dict | None = None):
        self.tag = tag
        self.value = value
        self.children = value
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        raise NotImplementedError

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})" """

import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_noprops(self):
        node = HTMLNode  (value="This is an html node")
        self.assertEqual (node.props_to_html(), "")

    def test_single_prop(self):
        node = HTMLNode (value="This is an html node", props={"class": "btn"})
        self.assertEqual (node.props_to_html(), ' class="btn"')

    def test_multiple_propse_sorted(self):
        node = HTMLNode(
            props={"target": "_blank", "href": "https://example.com"}
        )
        expected = ' href="https://example.com" target="_blank"'
        self.assertEqual (node.props_to_html(), expected)

    # LeafNode Tests
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"}).to_html()
        self.assertEqual(node, '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_to_html_b(self):
        node = LeafNode("b", "Hello, world!")
        self.assertEqual(node.to_html(), "<b>Hello, world!</b>")

    # ParentNode Tests
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
            )
        
    def test_to_html_with_no_children(self):
        parent_node = ParentNode("div", None)
        self.assertRaises(ValueError)

if __name__ == "__main__":
    unittest.main()

