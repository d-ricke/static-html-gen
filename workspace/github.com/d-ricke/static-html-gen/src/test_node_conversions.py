import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextType, TextNode
from node_conversions import text_node_to_html_node

class TestHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    def test_text_node_bold(self):
        node = TextNode("This is a text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.to_html(), "<b>This is a text node</b>")
    def test_text_node_italic(self):
        tn = TextNode("Italic text", TextType.ITALIC)
        hn = text_node_to_html_node(tn)
        self.assertEqual(hn.tag, "i")
        self.assertEqual(hn.value, "Italic text")

    def test_text_node_code(self):
        tn = TextNode("code()", TextType.CODE)
        hn = text_node_to_html_node(tn)
        self.assertEqual(hn.tag, "code")
        self.assertEqual(hn.value, "code()")

    def test_text_node_link(self):
        tn = TextNode("Google", TextType.LINK, url="https://google.com")
        hn = text_node_to_html_node(tn)
        self.assertEqual(hn.tag, "a")
        self.assertEqual(hn.value, "Google")
        self.assertEqual(hn.props, {"href": "https://google.com"})

    def test_text_node_image(self):
        tn = TextNode("Image alt", TextType.IMAGE, url="image.png")
        hn = text_node_to_html_node(tn)
        self.assertEqual(hn.tag, "img")
        self.assertEqual(hn.value, "")
        self.assertEqual(hn.props, {"src": "image.png", "alt": "Image alt"})

    def test_text_node_unknown_type(self):
        class FakeType:
            pass
        tn = TextNode("Some text", FakeType())
        with self.assertRaises(ValueError):
            text_node_to_html_node(tn)

if __name__ == "__main__":
    unittest.main()