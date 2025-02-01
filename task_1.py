import Binary_Tree

tree = Binary_Tree.Node()

root = Binary_Tree.insert(tree, 3)
root = Binary_Tree.insert(tree, 2)
root = Binary_Tree.insert(tree, 4)
root = Binary_Tree.insert(tree, 7)
root = Binary_Tree.insert(tree, 6)
root = Binary_Tree.insert(tree, 8)

print(root)



# Функція для знаходження найбільшого значення в дереві
def find_max(root):
    current = root
    while current.right:
        current = current.right
    return current.val

print("Найбільше значення:", find_max(root))