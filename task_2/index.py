class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def find_min_value(node):
    if node is None:
        return None

    current = node
    while current.left is not None:
        current = current.left
    return current.value

# Приклад використання:
# Створимо просте BST
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(20)
root.left.left = TreeNode(2)
root.left.right = TreeNode(8)

# Знайдемо найменше значення
min_value = find_min_value(root)
print("Найменше значення у дереві:", min_value)
