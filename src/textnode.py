from enum import Enum

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "img"

class TextNode():

    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type.value
        self.url = url

    def __eq__(self, node_2):
        if self.text == node_2.text:
            if self.text_type == node_2.text_type:
                if self.url == node_2.url:
                    return True

        return False

    def __repr__(self):
        return f'TextNode({self.text}, {self.text_type}, {self.url})'