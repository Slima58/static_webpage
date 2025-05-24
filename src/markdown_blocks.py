from enum import Enum
from htmlnode import (
    LeafNode,
    ParentNode,
)

from separate_text_to_nodes import text_to_textnodes
from textnode import text_node_to_html_node

import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

class BlockNode:
    def __init__(self, text_nodes, block_type):
        self.text_nodes = text_nodes
        self.block_type = block_type

    def __repr__(self):
        return f"BlockNode({self.text_nodes}, {self.block_type})"

def markdown_to_blocks(markdown):
    md = markdown.strip()
    lines = md.split("\n\n")
    new_lines = []
    for line in lines:
        if line == "":
            continue
        if line[0] == "\n":
            new_lines.append(line[1:])
        else:
            new_lines.append(line)
    return new_lines

def block_to_blocktype(block):
    lines = block.split("\n")

    if re.match(r"^#{1,6} .*", block):
        return BlockType.HEADING
    if block[:3] == "```" and block[-3:] == "```":
        return BlockType.CODE
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if block[:2] == "- ":
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH
    
def blocktype_to_htmlnode(block):
    btext_not_list = block.text_nodes.replace("\n", " ")
    if block.block_type == BlockType.QUOTE:
        return LeafNode(
            "blockquote",
            btext_not_list[2:],
            None
            )
        #return ParentNode(
        #    "blockquote",
        #    [LeafNode("p", btext_not_list[2:], None) ]
        #    )
    if block.block_type == BlockType.UNORDERED_LIST:
        lines = [text_to_textnodes(item[2:]) for item in block.text_nodes.split("\n")]
        child_Html_Nodes = []
        for line in lines:
            child_Html_Nodes.append(
                list( map(text_node_to_html_node, line) )
            )
        parent_Html_Nodes = [ParentNode("li", item, None) for item in child_Html_Nodes]
        grandparent_Html_Node = ParentNode("ul", parent_Html_Nodes, None)

        return grandparent_Html_Node

        #return ParentNode(
        #    "ul",
        #    None,
        #    [ LeafNode("li", item[2:]) for item in block.text.split("\n") ]
        #)
    if block.block_type == BlockType.ORDERED_LIST:
        lines = [text_to_textnodes(item[3:]) for item in block.text_nodes.split("\n")]
        child_Html_Nodes = []
        for line in lines:
            child_Html_Nodes.append(
                list( map(text_node_to_html_node, line) )
            )
        parent_Html_Nodes = [ParentNode("li", item, None) for item in child_Html_Nodes]
        grandparent_Html_Node = ParentNode("ol", parent_Html_Nodes, None)

        return grandparent_Html_Node

        #return ParentNode(
        #    "ol",
        #    None,
        #    [ LeafNode("li", item[3:]) for item in block.text.split("\n") ]
        #)
    if block.block_type == BlockType.CODE:
        #block_text_parsed = "\n".join(block.text_nodes.split("\n")[1:-1])
        return ParentNode(
            "pre",
            [LeafNode("code", block.text_nodes[4:-3], None)],
            None
        )
    if block.block_type == BlockType.HEADING:
        block_title_text = block.text_nodes.replace("#", "")[1:]
        return LeafNode(
            f"h{block.text_nodes.count("#")}",
            block_title_text,
            #{"id" : block_title_text.replace(" ", "-")}
            None
        )
    if block.block_type == BlockType.PARAGRAPH:
        #block.text_nodes.remove("\n")
        ###
        #cchild_text_nodes = text_to_textnodes(block.text_nodes.replace("\n", " "))
        child_text_nodes = text_to_textnodes(btext_not_list)
        child_Html_Nodes = list(
            map( text_node_to_html_node, child_text_nodes )
        )
        return ParentNode("p", child_Html_Nodes, None)

