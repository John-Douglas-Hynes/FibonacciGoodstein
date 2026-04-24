class tree:
    def __init__(self, val = 0, children = []):
        self.val = val
        self.children = children
    
    def pretty_print(self, node, depth_string = ''):
        print(f"{depth_string} {node.val}")
        for chld in node.children:
            self.pretty_print(chld, depth_string + ' ')

    def fibonacci_print(self, node, depth_string = ''):
        if node.val == 0:
            print(f"{depth_string} F_")
        elif node.val > 0:
            print(f"{depth_string} F{{{node.val}}}")
        for chld in node.children:
            self.fibonacci_print(chld, depth_string + '  ')

### Testing
#root = tree(0, [tree(2, []), tree(0, [tree(5, []), tree(6, [])]), tree(4, [])])
#root.fibonacci_print(root, '')
