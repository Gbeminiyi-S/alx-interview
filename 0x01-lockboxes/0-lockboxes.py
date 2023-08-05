#!/usr/bin/python3
""" This Module contains a function `canUnlockAll` """


def canUnlockAll(boxes):
    """Determines if all the boxes can be opened"""

    if type(boxes) != list:
        return False
    elif boxes == []:
        return True

    boxesLength = len(boxes)
    freeKeys = [0]
    usedKeys = set()

    while freeKeys:
        box = freeKeys.pop()
        usedKeys.add(box)

        if type(boxes[box]) != list:
            return False

        for key in boxes[box]:
            if (key < boxesLength) and (key not in freeKeys) and\
                    (key not in usedKeys):
                freeKeys.append(key)

    return len(usedKeys) == len(boxes)
