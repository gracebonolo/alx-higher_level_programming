#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """Delete item at a specific position in the list."""
    if idx < 0 or idx >= len(my_list):
        return my_list

    new_list = []
    for i, elem in enumerate(my_list):
        if i != idx:
            new_list.append(elem)

    return new_list
