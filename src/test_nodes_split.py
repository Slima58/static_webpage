import unittest
from textnode import TextType, TextNode
from markdown_object_parse import split_nodes_image, split_nodes_link

class TestNodeSplit (unittest.TestCase):
    def test_image_node_split(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_image_node_split_start(self):
        node = TextNode(
            "![image](https://i.imgur.com/zjjcJKZ.png) This is an image and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" This is an image and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_link_node_split(self):
        node = TextNode(
            "This is a [link](https://google.com) and this is [bootdev](https://boot.dev) Now lets have some fun.",
            TextType.TEXT
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://google.com"),
                TextNode(" and this is ", TextType.TEXT),
                TextNode("bootdev", TextType.LINK, "https://boot.dev"),
                TextNode(" Now lets have some fun.", TextType.TEXT)
            ],
            new_nodes,
        )

    def test_link_node_split_start(self):
        node = TextNode(
            "[link](https://google.com) and this is [bootdev](https://boot.dev) Now lets have some fun.",
            TextType.TEXT
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("link", TextType.LINK, "https://google.com"),
                TextNode(" and this is ", TextType.TEXT),
                TextNode("bootdev", TextType.LINK, "https://boot.dev"),
                TextNode(" Now lets have some fun.", TextType.TEXT)
            ],
            new_nodes,
        )
