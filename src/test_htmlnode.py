import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node1 = HTMLNode("a", "link", None, {"href": "https://boot.dev","target": "_blank"}) 
        node2 = HTMLNode("p", None, "some text", {"href": "https://programmerenjoyer.com"})
        node3 = HTMLNode(None, "title", None, {"href": "https://somelink.org"})
         
        result1 = node1.props_to_html()
        result2 = node2.props_to_html()
        result3 = node3.props_to_html()

        self.assertIn('href="https://boot.dev"', result1)
        self.assertIn('target="_blank"', result1)
        self.assertIn('href="https://programmerenjoyer.com"', result2)
        self.assertIn('href="https://somelink.org"', result3)

    def test_leaf_to_html_link(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com">Click me!</a>'
        )
    
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

if __name__ == "__main__":
    unittest.main()
