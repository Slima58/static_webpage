import re
from textnode import *
from textnode import TextNode, TextType

def extract_markdown_images(text):
    match = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return match

def extract_markdown_links(text):
    match = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return match

def split_nodes_image(old_nodes):
    im_re = re.compile(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)")
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        split_nodes = []
        node_text = node.text
        match = re.search(im_re, node_text)
        if match:
            sections = re.split(im_re, node_text, maxsplit=1)
            link_and_text = tuple(sections[1:3])
            sections = [sections[0], link_and_text, sections[-1] ]
            for i in range(len(sections)):
                if sections[i] == "":
                    continue
                if type(sections[i]) == type(()):
                    split_nodes.append(
                        TextNode(sections[i][0], TextType.IMAGE, sections[i][-1])
                    )
                elif i == (len(sections) - 1):
                    l_node = TextNode(sections[i], TextType.TEXT)
                    split_nodes.extend(
                        split_nodes_image(
                            [l_node]
                            )  
                    )
                    #print(new_nodes)
                else:
                    split_nodes.append(
                        TextNode(sections[i], TextType.TEXT)
                    )
            new_nodes.extend(split_nodes)
            #print(new_nodes)
        else:
            new_nodes = [node]
    return new_nodes


def split_nodes_link(old_nodes):
    im_re = re.compile(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)")
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        split_nodes = []
        node_text = node.text
        match = re.search(im_re, node_text)
        if match:
            sections = re.split(im_re, node_text, maxsplit=1)
            #print(sections)
            link_and_text = tuple(sections[1:3])
            sections = [sections[0], link_and_text, sections[-1] ]
            for i in range(len(sections)):
                if sections[i] == "":
                    continue
                if type(sections[i]) == type(()):
                    split_nodes.append(
                        TextNode(sections[i][0], TextType.LINK, sections[i][-1])
                    )
                elif i == (len(sections) - 1):
                    l_node = TextNode(sections[i], TextType.TEXT)
                    split_nodes.extend(
                        split_nodes_link(
                            [l_node]
                            )  
                    )
                    #print(split_nodes)
                else:
                    split_nodes.append(
                        TextNode(sections[i], TextType.TEXT)
                    )
            new_nodes.extend(split_nodes)
            #print(new_nodes)
        else:
            new_nodes = [node]
    return new_nodes
