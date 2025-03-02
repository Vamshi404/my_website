from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if not tag:
            raise ValueError("ParentNode must have a tag.")
        if not children:
            raise ValueError("ParentNode must have children.")
        
        super().__init__(tag, value=None, children=children, props=props)
    
    def to_html(self):
        if not self.tag:
            raise ValueError("ParentNode must have a tag.")
        if not self.children:
            raise ValueError("ParentNode must have children.")
        
        # Render the opening tag with props (if any)
        opening_tag = f"<{self.tag}{' ' + self.props_to_html() if self.props else ''}>"
        
        # Recursively render the children
        children_html = ''.join([child.to_html() for child in self.children])
        
        # Render the closing tag
        closing_tag = f"</{self.tag}>"
        
        # Return the complete HTML string
        return f"{opening_tag}{children_html}{closing_tag}"