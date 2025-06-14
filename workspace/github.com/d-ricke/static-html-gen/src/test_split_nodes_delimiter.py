import unittest

from textnode import TextNode, TextType
from split_nodes_delimiter import split_nodes_delimiter


class TestSplitNodesDelimiter(unittest.TestCase):

    def test_code_split(self):
        input_nodes = [TextNode("This is `code` and `more` code", TextType.TEXT)]
        result = split_nodes_delimiter(input_nodes, "`", TextType.CODE)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" and ", TextType.TEXT),
            TextNode("more", TextType.CODE),
            TextNode(" code", TextType.TEXT)
        ]
        self.assertEqual(result, expected)

    def test_bold_split(self):
        input_nodes = [TextNode("Here is **bold** text", TextType.TEXT)]
        result = split_nodes_delimiter(input_nodes, "**", TextType.BOLD)
        expected = [
            TextNode("Here is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT)
        ]
        self.assertEqual(result, expected)

    def test_italic_split(self):
        input_nodes = [TextNode("Some _italic_ stuff", TextType.TEXT)]
        result = split_nodes_delimiter(input_nodes, "_", TextType.ITALIC)
        expected = [
            TextNode("Some ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" stuff", TextType.TEXT)
        ]
        self.assertEqual(result, expected)

    def test_no_delimiters(self):
        input_nodes = [TextNode("No formatting here", TextType.TEXT)]
        result = split_nodes_delimiter(input_nodes, "**", TextType.BOLD)
        self.assertEqual(result, input_nodes)

    def test_odd_number_of_delimiters_raises(self):
        input_nodes = [TextNode("This is `broken syntax", TextType.TEXT)]
        with self.assertRaises(Exception):
            split_nodes_delimiter(input_nodes, "`", TextType.CODE)

    def test_non_text_node_passthrough(self):
        input_nodes = [TextNode("img", TextType.IMAGE)]
        result = split_nodes_delimiter(input_nodes, "**", TextType.BOLD)
        self.assertEqual(result, input_nodes)


if __name__ == "__main__":
    unittest.main()
