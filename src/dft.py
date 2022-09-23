"""A module for depth-first (in-order) traversal of trees."""

from typing import Iterable
from tree import T


def in_order(t: T | None) -> Iterable[int]:
    return in_order_simple(t)

def in_order_simple(t: T | None) -> Iterable[int]:
    """In-order traversal of a tree.

    >>> tree = T(2, T(1, None, None), T(4, T(3, None, None), T(5, None, None)))
    >>> list(in_order(tree))
    [1, 2, 3, 4, 5]
    """
    stack = []
    if t:
        stack.append(t)
    
    def pushIfExists(*elements):
        for e in elements:
            if e is not None:
                stack.append(e)

    while stack:
        match stack.pop():
            case T(val, left, right):
                pushIfExists(right, val, left)
            case val:
                yield val












#Don't mind my brainstorm here

#TODO make None into pointer to first where it is left child
# parent.left = parent if parent.left = None
# can go up step by step, but takes quadratic
# save root, find the ones that points to it? repeat for root children etc. 
#   Bad: Then multiple will point at same  

#Algorithm
#Go most left while finding height of three
#While saving highest point, move in subtree 
#Nope, that assumes ballanced
#Save height of subtree instead

#Know everything to left
# Can delete/reuse memory in subtree when done 


#What happens if you point at parent instead? 

#Can make algorithm very simple, but very slow


def in_order_memory(t: T | None) -> Iterable[int]:
    """In-order traversal of a tree.

    >>> tree = T(2, T(1, None, None), T(4, T(3, None, None), T(5, None, None)))
    >>> list(in_order(tree))
    [1, 2, 3, 4, 5]
    """
    node = t
    output = []
    subtreeHeight = 0
    parent = None

    while True:
        while node:
            parent = node
            node = node.left
            subtreeHeight += 1
        output.append(parent.val)





