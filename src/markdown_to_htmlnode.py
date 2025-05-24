from htmlnode import (
    ParentNode,
    LeafNode,
)

from markdown_blocks import (
    BlockType,
    BlockNode,
    markdown_to_blocks,
    block_to_blocktype,
    blocktype_to_htmlnode
)

from separate_text_to_nodes import (
    markdown_inline_parser,
    text_to_textnodes,
)

def markdown_to_html_node(text):
    m_blocks = markdown_to_blocks(text)
    block_nodes = [ BlockNode( block, block_to_blocktype(block) ) for block in m_blocks]
    html_nodes = [ blocktype_to_htmlnode(block) for block in block_nodes]  
    #print(html_nodes)
    #return ''.join([node.to_html() for node in html_nodes])
    html_page = ParentNode("div", html_nodes, None)
    return html_page


    
        

