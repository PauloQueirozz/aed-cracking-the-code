def lowest_common_ancestor(root, value1, value2):
    node = root
    while node is not None:
        val = node.get_value()
        if value1 < val and value2 < val:
            node = node.get_left_child()
        elif value1 > val and value2 > val:
            node = node.get_right_child()
        else:
            return val
    return -1
