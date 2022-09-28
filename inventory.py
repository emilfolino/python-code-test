#!/usr/bin/env python3

'''
Inventory functions
'''

def pick(myInventory, item, indx=None):
    '''
    Puts item(s) into inventory
    '''
    items = item.split(',')

    if indx is not None:
        indx = int(indx)

        if indx > len(myInventory):
            print(f'Error! Index {indx} is out of range.')    
        
        else:
            myInventory[:] = myInventory[:indx] + items + myInventory[indx:]
            print(f'Added {" and ".join(items)} at index {indx}')

    else:
        myInventory += items
        print(f'Added {" and ".join(items)} to inventory')

    return myInventory

def inventory(myInventory, start=0, end=None):
    '''
    Displays inventory
    '''
    if end is None:
        end = len(myInventory)
    else:
        start = int(start)
        end = int(end)

    print(f'Inventory has {len(myInventory)} items: {myInventory[start:end]}')

def drop(myInventory, item):
    '''
    Removes item from inventory
    '''
    try:
        myInventory.remove(item)
        print(f'Removed {item} from inventory')

    except ValueError:
        print(f'Error! Could not find {item} in inventory')

    return myInventory

def swap(myInventory, itemA, itemB):
    '''
    Swaps items in inventory
    '''
    badItems = []
    testInventory = myInventory[:]

    # check if items exist
    if not itemA in testInventory:
        badItems.append(itemA)
    else:
        testInventory.remove(itemA)

    if not itemB in testInventory:
        badItems.append(itemB)

    # if no bad items, do the swap
    if badItems == []:
        indxA = myInventory.index(itemA)
        indxB = myInventory.index(itemB)
        
        temp = myInventory[indxA]
        myInventory[indxA] = myInventory[indxB]
        myInventory[indxB] = temp

        print(f'Swapped {itemA} and {itemB}')

    else:
        print(f'Error! Could not find {" or ".join(badItems)} in inventory')

    return myInventory
