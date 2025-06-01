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

from htmlnode import HTMLNode


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

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")


if __name__ == "__main__":
    unittest.main()

