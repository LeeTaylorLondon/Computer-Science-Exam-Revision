# Author: Lee Taylor
# hashing.linearprobe.py
from typing import NoReturn, List, Tuple, Optional


class LinearProbe:
    def __init__(self, size:int=11, arr:List[int]=None):
        self.size = size
        self.values = [None for x in range(size)]
        if (arr != None):
            for elm in arr:
                self.insert(elm)

    def __repr__(self) -> str:
        rv = ''
        for elm in self.values:
            if (elm != None): rv = rv + ' ' + str(elm)
            else: rv = rv + ' -'
        return rv[1:]

    def __str__(self) -> str:
        rv = ''
        for elm in self.values:
            if (elm != None):
                rv = rv + ' ' + str(elm)
            else:
                rv = rv + ' -'
        return rv[1:]

    def __setitem__(self, key:int, value:int) -> NoReturn:
        self.values[key] = value

    def h(self, elm:Optional[int]=None) -> int:
        """ Hash function used to determine locations of passed data """
        if (elm == None): return -1
        return elm % self.size

    def insert(self, elm:int) -> NoReturn:
        # Ensures elm passed is of type int & calculates location
        if (type(elm) != int):
            raise TypeError(f"Element, {elm}, must be of type int!")
        if (elm in self.values):
            raise TypeError(f"No duplicates!")
        location = elm % self.size
        # From calculated location to end check if there is a space for elm
        for i in range(location, self.size):
            if (self.values[i] == None):
                self.values[i] = elm
                return
        # From start to calculated location check if there is a space for elm
        for i in range(0, location):
            if (self.values[i] == None):
                self.values[i] = elm
                return
        # This is only reached if there is no space for the passed element
        print(f"No space for {elm}, not inserted!")

    def search(self, elm:int) -> int:
        """ Searches for an element only returns index~location """
        # Ensures passed elm is of type int calculates location
        if (type(elm) != int):
            raise TypeError(f"Element, {elm}, must be of type int!")
        location = elm % self.size
        # Check from location to end
        for i in range(location, self.size):
            if (self.values[i] == None): return -1
            if (self.values[i] == elm): return i
        # Check from start to location
        for i in range(0, self.size):
            if (self.values[i] == None): return -1
            if (self.values[i] == elm): return i
        # This is only reached if the searched failed
        return -1

    def search_traced(self, elm:int) -> Tuple[List[str], int]:
        """ Search for an element where each action is traced & returned & location """
        # Ensures passed elm is of type int calculates location
        rv = []
        if (type(elm) != int):
            raise TypeError(f"Element, {elm}, must be of type int!")
        location = elm % self.size
        # Append trace
        rv.append(f"Search for {elm}")
        rv.append(f"H({elm}) = {location}")
        elements = 'Search right: '
        # Check from location to end
        for i in range(location, self.size):
            if (self.values[i] == None):
                elements = elements + 'empty space so not found'
                rv.append(elements)
                return rv, -1
            if (self.values[i] == elm):
                elements = elements + f"found at index {i}"
                rv.append(elements)
                return rv, i
            else:
                elements = elements + f"{elm}!={self.values[i]}, "
        # Check from start to location
        for i in range(0, self.size):
            if (self.values[i] == None):
                elements = elements + 'empty space so not found'
                rv.append(elements)
                return rv, -1
            if (self.values[i] == elm):
                elements = elements + f"found at index {i}"
                rv.append(elements)
                return rv, i
            else:
                elements = elements + f"{elm}!={self.values[i]}, "
        # This is only reached if the searched failed
        rv.append(elements)
        rv.append(f"not found")
        return rv, -1

    def delete(self, elm:int) -> bool:
        """
        method delete -> Deletes a value from the LinearProbe if found.

        Where a value deleted shares the same hash value as another
        value in the Linear Probe the other value is shifted.

        The process of shifting either occurs or not at all.
        Variable 'shift' indicates whether shifting occurred or not and is returned
        for use in a question. See questions.py function deletion for more details.
        """
        # Location of element to delete & init replacement index var
        moved = {}
        del_location = -1
        # Variable shift see method doc-string for explanation
        shifted = False
        for i,v in enumerate(self.values):
            if (v == elm): del_location = i
        if (del_location == -1): print(f"{elm} does not exist!")
        replacement = -1
        while (replacement != None):
            # Iter over <del+1> -> <end>
            for i in range(del_location+1, self.size):
                # if (a[i] == None) then a[i]=None & return shifted
                if (self.values[i] == None):
                    self.values[del_location] = None
                    return shifted
                # if (a[i] = H(k)) && (not moved) && (not in base-pos)
                if (self.h(self.values[i]) == self.h(elm)) and \
                        (self.values[i] not in moved) and (self.h(self.values[i]) != i):
                    replacement = i
                    break
            # If no replacement found in <del+1> -> <end> then
            # check from <start> -> <del-1>
            if (replacement == -1):
                # Iter over <start> -> <del-1>
                for i in range(0, del_location-1):
                    # if (a[i] == None) then a[i]=None & return shifted
                    if (self.values[i] == None):
                        self.values[del_location] = None
                        return shifted
                    # if (a[i] = H(k)) && (not moved) && (not in base-pos)
                    if (self.h(self.values[i]) == self.h(elm)) and \
                            (self.values[i] not in moved) and (self.h(self.values[i]) != i):
                        replacement = i
                        break
            # If a replacement is found elm to del is overwritten
            if (replacement != -1):
                # Values are being 'Shifted' therefore shifted = True
                shifted = True
                # Replace value
                self.values[del_location] = self.values[replacement]
                # Tag replacement value as 'moved'
                moved.update({self.values[del_location]: self.values[del_location]})
                # Index to delete is updated with replacement
                del_location = replacement
                # Value to delete is updated with value at replacement
                elm = self.values[del_location]
                # Reset replacement variable
                replacement = -1
            # If no replacement is found index del_location is emptied
            # While-loop is broken by setting var replacement to None
            else:
                replacement = None
                self.values[del_location] = None
        return shifted
