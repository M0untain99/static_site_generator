from textnode import TextNode, TextType

def main():
    test_node = TextNode("Test Text", TextType.LINK, "https://www.google.com")
    print(test_node.__repr__())

main()