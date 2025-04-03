from enum import Enum
from leafnode import LeafNode

class TextType(Enum):
    BOLD = "bold"
    ITALIC = "italic" 
    CODE = "code" 
    LINK = "link" 
    IMAGE = "image"
    TEXT = "text"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
        return

    def __eq__(self, other) -> bool:
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

    def get_text_type(self) -> TextType:
        return self.text_type

    def get_text(self) -> str:
        return self.text
    
    def get_url(self) -> str | None:
        return self.url

def text_node_to_html_node(text_node):
    match text_node.get_text_type():
        case TextType.TEXT:
            return LeafNode(None, text_node.get_text())
        case TextType.BOLD:
            return LeafNode("b", text_node.get_text())
        case TextType.ITALIC:
            return LeafNode("i", text_node.get_text())
        case TextType.CODE:
            return LeafNode("code", text_node.get_text())
        case TextType.LINK:
            return LeafNode("a", text_node.get_text(), {"href": f"{text_node.get_url()}",})
        case TextType.IMAGE:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        case _:
            raise Exception("Type not in TextType Enum")
