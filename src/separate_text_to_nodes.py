from markdown_object_parse import split_nodes_image, split_nodes_link 
from textnode import TextNode, TextType
from inline_markdown import split_nodes_delimiter 


def markdown_inline_parser(nodes):
    delimiters = {
        "**" : TextType.BOLD,
        "_" : TextType.ITALIC,
        "`" : TextType.CODE
    }
    for k, v in delimiters.items():
        nodes = split_nodes_delimiter(nodes, k, v)
    return nodes


def text_to_textnodes(text):
    node = [ TextNode(text, TextType.TEXT) ]
    nodes = split_nodes_image(node) 
    nodes = split_nodes_link(nodes)
    nodes = markdown_inline_parser(nodes)
    return nodes
