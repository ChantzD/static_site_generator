from enum import Enum
from htmlnode import *
from inline import text_to_textnodes
from textnode import TextNode, text_node_to_html_node
from parentnode import ParentNode
from leafnode import LeafNode

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def markdown_to_html_node(markdown):
    node_list = []
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case BlockType.HEADING:
                node_list.append(heading_to_node(block))
            case BlockType.QUOTE:
                node_list.append(quote_to_node(block))
            case BlockType.PARAGRAPH:
                node_list.append(paragraph_to_node(block))
            case BlockType.CODE:
                node_list.append(ParentNode("pre", [LeafNode("code", block.strip("`").lstrip("\n"))]))
            case BlockType.UNORDERED_LIST:
                node_list.append(ul_to_node(block))
            case BlockType.ORDERED_LIST:
                node_list.append(ol_to_node(block))
    return ParentNode("div", node_list)


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    child_nodes = []
    for node in text_nodes:
        child_nodes.append(text_node_to_html_node(node))
    return child_nodes

def ol_to_node(ol):
    child_nodes = []
    items = [line.split('. ', 1)[1] for line in ol.splitlines()]
    for item in items:
        if item == "":
            continue
        child_nodes.append(ParentNode("li", text_to_children(item.strip())))
    return ParentNode("ol", child_nodes)

def ul_to_node(ul):
    child_nodes = []
    items = ul.split("-")
    for item in items:
        if item == "":
            continue
        child_nodes.append(ParentNode("li", text_to_children(item.strip())))
    return ParentNode("ul", child_nodes)

def paragraph_to_node(para):
    return ParentNode("p", text_to_children(para.replace("\n", " ")))

def quote_to_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)

def heading_to_node(heading):
    heading_level = heading.count("#")
    tag = f"h{heading_level}"
    return ParentNode(tag, text_to_children(heading.strip("# ")))

def block_to_block_type(block):
    if block.startswith("#"):
        return BlockType.HEADING
    elif block.startswith("```"):
        return BlockType.CODE
    elif block.startswith(">"):
        return BlockType.QUOTE
    elif block.startswith("-"):
        return BlockType.UNORDERED_LIST
    elif block[:1].isdigit() and block[1] == ".":
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH

    
def markdown_to_blocks(markdown):
    list_of_blocks = markdown.split("\n\n")
    list_of_blocks = [x.strip() for x in list_of_blocks]
    index = 0
    for block in list_of_blocks:
        if block == "":
            list_of_blocks.pop(index)
        index += 1

    return list_of_blocks


