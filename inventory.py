""" Marvins backback - list functions"""

def inventory(backpack: list, start = None, stop = None):
    """ prints the number of items in the backpack and their names"""
    if start is None and stop is None:
        print("The backpack contains {} items:".format(len(backpack)))
        print(backpack)
    else:
        print(", ".join(backpack[start:stop]))

def pick(backpack: list, item, index_str: int = None):
    """ puts item in backpack"""
    # 1. do index things
    index=0
    if index_str is not None:
        index = int(index_str)
        if index > len(backpack):
            print("Error: index {} too high".format(index))
            return backpack
    elif index_str is None: 
        index = len(backpack)
    
    # 2. insert item(s)
    items = item.split(",")
    i = 0
    for e in items:
        backpack.insert(index + i, e)
        i += 1
    print("You added {} to the bag at index {}.".format(items, index))
    return backpack

def drop(backpack: list, item):
    """ drops item from backpack"""
    try:
        backpack.remove(item)
        print("{} was dropped from Marvins backpack".format(item))
        return backpack
    except ValueError:
        print("Error: No {} found in Marvins backpack".format(item))
        return backpack

def swap(backpack: list, item1, item2):
    """ swaps positions of item 1 and 2 in backpack"""
    indexes = []
    for i, item in enumerate(backpack):
        if item in (item1,item2):
            indexes.append(i)
    if len(indexes) < 2:
        print("Error: One or both of the items ({}, {}) not found in Marvins backpack".format(item1, item2))
        return backpack
    temp = backpack[indexes[0]]
    backpack[indexes[0]] = backpack[indexes[1]]
    backpack[indexes[1]] = temp 
    print("You swapped {} and {}.".format(item1, item2))
    return backpack
