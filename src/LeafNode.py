from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        # Ensuring no children for LeafNode
        if value is None:
            raise ValueError("LeafNode must have a value.")
        super().__init__(tag, value, children=None, props=props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value.")
        
        if self.tag:
            # Render an HTML tag with props if tag exists
            props_str = f" {self.props_to_html()}" if self.props else ""
            return f"<{self.tag}{props_str}>{self.value}</{self.tag}>"
        else:
            # If no tag, return raw text
            return self.value