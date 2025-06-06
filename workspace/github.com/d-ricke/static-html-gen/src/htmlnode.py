from __future__ import annotations

class HTMLNode():
    def __init__(self, tag=None, value: str | None=None, children: HTMLNode | None=[], props: dict | None = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if not self.props: 
            return ""
        
        return "".join(
            f' {key}="{value}"' for key, value in sorted(self.props.items())
        )

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode (HTMLNode):
    def __init__ (self, tag: str, value: str, props: dict | None=None):
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if self.value == None:
            raise Exception(ValueError)
        
        elif self.tag == None:
            return (self.value)
        
        else:
            return (f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>')
        
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode (HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if self.tag == None:
            raise ValueError
        
        elif not self.children:
            raise ValueError ("ParentNode requires children")
        
        else:
            children_html = "".join(child.to_html() for child in self.children)
            return (f'<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>')