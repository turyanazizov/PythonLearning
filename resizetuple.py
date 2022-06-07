tuple = ("hello", True, 5)

def resizeTuple(item):
    new_element = input("Enter new element: ")
    added_tuple = (new_element,)
    item = item+added_tuple
    return item


print(resizeTuple(tuple))
