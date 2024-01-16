#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """Replace all occurrences of 'search' by 'replace' in a new list."""
    return [replace if element == search else element for element in my_list]
