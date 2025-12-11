class HTMLNode():
    
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value 
        self.children = children
        self.props = props 

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        s = ""
        if self.props == None or len(self.props) == 0:
            return ""
        for key, value in self.props.items():
            s += f' {key}="{value}"'
        return s

    def __repr__(self):
        return f"tag={self.tag}, value={self.value}, children={self.children}, props={self.props}"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("No value")

        if self.tag == None:
            return self.value

        html_props = super().props_to_html()

        return f"<{self.tag}{html_props}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("No tag")
        
        if self.children == None:
            raise ValueError("No children")
        
        html_props = super().props_to_html()

        result = f"<{self.tag}{html_props}>"

        for child in self.children:
            result += child.to_html()

        result += f"</{self.tag}>"

        return result

