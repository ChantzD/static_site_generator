from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None) -> None:
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("All leaf nodes must have a value")
        elif self.tag == None:
            return self.value

        match self.tag:
            case "a":
                return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
            case _:
                return f"<{self.tag}>{self.value}</{self.tag}>"
