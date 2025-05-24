import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType, text_node_to_html_node


class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode("p", "BootDev", None, {"href": "https://www.google.com"})
        self.assertEqual(repr(node),
                         "HTMLNode(p, BootDev, None, {'href': 'https://www.google.com'})")

    def test_props(self):
        node = HTMLNode("p", "BootDev", None, {"href": "https://www.google.com",
                                               "targe" : "_blank"})
        self.assertEqual(
            node.props_to_html(),
            ' href="https://www.google.com" targe="_blank"'
        )

    def test_values(self):
        node = HTMLNode("p", "BootDev", None, {"href": "https://www.google.com",
                                               "targe" : "_blank"})
        self.assertEqual(
            node.tag, 
            "p"
        )
        self.assertEqual(
            node.value,
            "BootDev"
        )
        self.assertEqual(
            node.children,
            None
        )
        self.assertEqual(
            node.props,
            {
                "href": "https://www.google.com",
                "targe" : "_blank"
            }
        )

    def test_leaf_to_html_no_tag(self):
        self.assertEqual(
            LeafNode(None, "helllo world", None).to_html(),
            "helllo world"
        )

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href" : "https://www.google.com"})
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com">Click me!</a>',
        )

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, World!")
        self.assertEqual(node.to_html(), "<p>Hello, World!</p>")

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




if __name__ == "__main__":
    unittest.main()

