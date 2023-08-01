#!/usr/bin/python3
""" This Module contains a function `canUnlockAll` """


def canUnlockAll(boxes):
    """ Determines if all the boxes can be opened. Each
        box is numbered sequentially from 0 to n - 1 and
        each box may contain keys to the other boxes
    """

    if type(boxes) != list:
        return False

    openedBoxes = set()
    boxesLength = len(boxes)
    box = [0]

    while box:
        key = box.pop()
        openedBoxes.add(key)

        if type(boxes[key]) != list:
            return False

        for value in boxes[key]:
            if value < boxesLength and value not in openedBoxes:
                box.append(value)

    return len(openedBoxes) == len(boxes)
