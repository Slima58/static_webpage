from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        split_nodes = []
        sections = node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")

        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


#def markdown_to_blocks(markdown):
#    md = markdown.strip()
#    lines = md.split("\n\n")
#    new_lines = []
#    for line in lines:
#        if line == "":
#            continue
#        if line[0] == "\n":
#            new_lines.append(line[1:])
#        else:
#            new_lines.append(line)
#    return new_lines

