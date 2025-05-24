import unittest
from markdown_blocks import (
    markdown_to_blocks,
    BlockType, 
    block_to_blocktype,
)

from markdown_to_htmlnode import markdown_to_html_node

class TestMarkdownBlocks(unittest.TestCase):
    def test_markdown_block_separator(self):
        md = """This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items"""

        blocks = markdown_to_blocks(md)
        self.assertListEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_block_excessive_blines(self):
        md = """This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here


This is the same paragraph on a new line



- This is a list
- with items"""

        blocks = markdown_to_blocks(md)
        print(blocks)
        self.assertListEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here",
                "This is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_block_empty_lines(self):
        md = """
        This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here



This is the same paragraph on a new line



- This is a list
- with items
"""

        blocks = markdown_to_blocks(md)
        print(blocks)
        self.assertListEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here",
                "This is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

class TestMarkdownBlockTypes(unittest.TestCase):
    def test_markdown_block_ordered_lists(self):
        self.assertEqual(
            BlockType.ORDERED_LIST,
            block_to_blocktype("1. first item")
        )

    def test_markdown_block_unordered_lists(self):
        self.assertEqual(
            BlockType.UNORDERED_LIST,
            block_to_blocktype("- second item")
        )

    def test_markdown_block_quote(self):
        self.assertEqual(
            BlockType.QUOTE,
            block_to_blocktype("> this is a quote")
        )
        
    def test_markdown_block_code(self):
        self.assertEqual(
            BlockType.CODE,
            block_to_blocktype("``` print(this_code) ```")
        )

    def test_markdown_block_heading(self):
        self.assertEqual(
            BlockType.HEADING,
            block_to_blocktype("# heading")
        )
        self.assertEqual(
            BlockType.HEADING,
            block_to_blocktype("### heading")
        )
        self.assertEqual(
            BlockType.HEADING,
            block_to_blocktype("###### heading")
        )

    def test_markdown_block_paragraph(self):
        self.assertEqual(
            BlockType.PARAGRAPH,
            block_to_blocktype("this is a phragraph")
        )

class TestMarkdownToHTML(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>"
        )
    
    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_quote(self):
        md = """> this is a quote

this is a paragraph

> this is another quote
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
           html, 
            "<div><blockquote><p>this is a quote</p></blockquote><p>this is a paragraph</p><blockquote><p>this is another quote</p></blockquote></div>"
        )

    def test_unordered_list(self):
        md ="""this is a list

- one
- two
- three
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>this is a list</p><ul><li>one</li><li>two</li><li>three</li></ul></div>"
        )

    def test_ordered_list(self):
        md ="""this is a list

1. one
2. two
3. three
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>this is a list</p><ol><li>one</li><li>two</li><li>three</li></ol></div>"
        )

    def test_headings(self):
        md = """
# title 1

### title 2

##### title 3
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><h1 id="title-1">title 1</h1><h3 id="title-2">title 2</h3><h5 id="title-3">title 3</h5></div>'
        )

if __name__ == "__main__":
    unittest.main()
