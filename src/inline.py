from textnode import TextNode, TextType
from typing import List, Tuple
import re

def text_to_textnodes(text):
    return split_nodes_delimiter(split_nodes_delimiter(split_nodes_delimiter(split_nodes_link(split_nodes_image([TextNode(text, TextType.TEXT)])), "**", TextType.BOLD), "_", TextType.ITALIC), "`", TextType.CODE)

def split_nodes_delimiter(old_nodes: List[TextNode], delimiter: str, text_type: TextType):
    new_nodes = []
    for node in old_nodes:
        if node.get_text_type() == TextType.TEXT:
            if not node.get_text().count(delimiter) % 2 == 0:
                raise Exception("Invalid Markdown syntax")
            split_line = node.get_text().split(delimiter)
            for i in range(0, len(split_line)):
                if i % 2 == 0:
                    new_nodes.append(TextNode(split_line[i], TextType.TEXT))
                else:
                    new_nodes.append(TextNode(split_line[i], text_type))
        else:
            new_nodes.append(node)

    return new_nodes

# def split_nodes_image(old_nodes):
#     new_nodes = []
#     for node in old_nodes:
#         images_info = extract_markdown_images(node.get_text())
#         if len(images_info) > 0:
#             text = node.get_text()
#             for i in range(0, len(images_info)):
#                 node1, node2, text = image_splitter(text, images_info[i])
#                 new_nodes.append(node1)
#                 new_nodes.append(node2)
#                 if i == len(images_info) - 1 and not text == "":
#                     new_nodes.append(TextNode(text, TextType.TEXT))
#         else:
#             new_nodes.append(node)
#     return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        images = extract_markdown_images(original_text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(
                TextNode(
                    image[0],
                    TextType.IMAGE,
                    image[1],
                )
            )
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        images_info = extract_markdown_links(node.get_text())
        if len(images_info) > 0:
            text = node.get_text()
            for i in range(0, len(images_info)):
                node1, node2, text = link_splitter(text, images_info[i])
                new_nodes.append(node1)
                new_nodes.append(node2)
                if i == len(images_info) - 1 and not text == "":
                    new_nodes.append(TextNode(text, TextType.TEXT))
        else:
            new_nodes.append(node)
    return new_nodes
def extract_markdown_images(text: str) -> List[Tuple[str, str]]:
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def extract_markdown_links(text: str) -> List[Tuple[str, str]]:
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def image_splitter(text="", info=[] ):
    sections = text.split(f"![{info[0]}]({info[1]})", 1)
    return TextNode(sections[0], TextType.TEXT), TextNode(info[0], TextType.IMAGE, info[1]), sections[1]
    
def link_splitter(text="", info=[] ):
    sections = text.split(f"[{info[0]}]({info[1]})", 1)
    return TextNode(sections[0], TextType.TEXT), TextNode(info[0], TextType.LINK, info[1]), sections[1]
