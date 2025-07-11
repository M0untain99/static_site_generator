
class HTMLNode():

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag  # The HTML Tag
        self.value = value  # The value in the HTML tag
        self.children = children  # List of HTML Node objects that are children of this node
        self.props = props  # Dictionary for attributes i.e. {"href": "https://www.google.com"}

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        
        output_string = ""

        for item in self.props:
            pair_string = f' {item}="{self.props[item]}"'
            output_string += pair_string

        return output_string

    def __repr__(self):
        print(f'''Tag: {self.tag}
        Value: {self.value}
        Number of Children: {len(self.children)}
        Props: {self.props}''')

