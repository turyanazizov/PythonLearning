tuple_ = ("hello", True, 5)
new_element = input("Enter new element: ")

def resizeTuple(item):
    item = (item,)
    return tuple_+item

print(resizeTuple(new_element))
