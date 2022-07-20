# Question from https://docs.google.com/document/d/1d0piZv7Hsog3IdOxvqZ569v1NSp6sHC76o_17gO0z5Q/edit

from collections import deque

def right_side_view(root):
    if not root:
        return []
    to_visit = deque([(root,0)])
    result = [ ]
    previous_level = -1
    while to_visit:
        current, current_level = to_visit.popleft()
        if current.left:
            to_visit.append((current.left, current_level + 1))
        if current.right:
            to_visit.append((current.right, current_level + 1))
        if current_level != previous_level:
            result.append(current.val)
        else:
            result[current_level] = current.val
        previous_level = current_level
    return result