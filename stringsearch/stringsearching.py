# stringsearching.py
# Author: Lee Taylor
from typing import NoReturn, Tuple, List, Optional


def bruteforce(t:str, p:str) -> Tuple[int, int]:
    """ Returns location, & no. of comparisons both of type int """
    comps, offset, rv = 0, 0, None
    while (rv == None) and not(offset > len(t) - len(p)):
        for i in range(len(p)):
            comps += 1
            if (p[i] != t[i+offset]):
                offset += 1
                break
            elif (i == len(p) - 1) and (p[i] == t[i+offset]):
                return offset, comps
    return -1, comps



def find_next(p: str) -> int:
    """
    Assuming the last character is a failure next value is returned

    Note: there is a significantly more efficient method to achieve this
    this simply follows the 'by-hand' rules provided in the lecture videos.
    """
    if (len(p) == 1): return -1
    # Init, answer (return value), & offset (used to shift the pattern)
    answer = None
    offset = 1
    # While there is no answer and the offset does not point out of bounds
    while (answer == None) and (offset != len(p)):
        # If char at p[offset] equals p starting char begin iterative comparison
        if (p[offset] == p[0]):
            pslice = p[offset:]
            # Compare pattern chars to chars in slice of pattern (shifted pattern)
            for i,char in enumerate(pslice):
                # If chars do not match ...
                if (char != p[i]):
                    # ... and i points to the end then ans = i
                    if (i == len(pslice)-1):
                        answer = i
                        break
                    # ... and i does not point to the end then skip to next (shift)
                    else:
                        offset += 1
                        break
                # If the ending chars match then skip to next
                elif (char == p[i]) and (i == len(pslice)-1):
                    offset += 1
        # If last char of P != first char then ans is 0
        elif (offset == len(p) - 1) and (p[0] != p[-1]):
            answer = 0
        else:
            offset += 1
    if (answer == None):
        answer = -1
    return answer


def table(p: str, debug:bool=False) -> List[int]:
    table = []
    for i in range(len(p)):
        table.append(find_next(p[0:i+1]))
    if (debug):
        print(f"table('{p}') -> Return : {table}")  # Debug
    return table


def kmp_search(t: str, p: str, debug:bool=False) -> Tuple[int, int]:
    """
    Searches for a string within another string

    Note: there is a significantly more efficient method to achieve this
    this simply follows the 'by-hand' rules provided in the lecture videos.
    """
    # Init. table, answer, & offset value
    next_table = table(p)
    answer = None
    offset, next, comparisons = 0, 0, 0
    # While there is no answer, & offset does not point out of bounds
    while (answer == None) and not(offset > (len(t) - len(p))):
        comparisons += 1
        if (p[0] == t[offset]):
            # Begin iterative comparison of characters
            tslice = t[offset:]
            comparisons -= 1  # Prevents counting the first comparison twice
            for i,c in enumerate(p):
                # Shift i to next value
                if (i < next):
                    continue
                # Only count comparisons when i is at valid position
                comparisons += 1
                # If characters mismatch set new offset value & skip to next
                if (c != tslice[i]):
                    next = next_table[i]
                    offset += i - next_table[i]
                    break
                # If on last character of p and equal then answer was found
                elif (i == len(p) - 1) and (c == tslice[i]):
                    answer = offset
        else:
            offset += 1
    # If no answer was found
    if (answer == None):
        answer = -1
    # Debug
    if (debug):
        print(f"Find: '{p}' Within: '{t}'")
        print(f"Answer = {answer}, Comparisons = {comparisons}\n")
    return answer, comparisons


def kmp_search_traced(t: str, p: str, debug:bool=False) -> Tuple[Optional[int], int, List[str]]:
    """
    Returns formatted answer:
        <t>
        <p> fails index <i>, next is <table[i]> (comps=<i-next>)
        ...
        Total Comparisons is <sum of comp(s)>
    """
    # Init trace, & comparisons
    trace = [t]
    trace_comps_arr = []
    # Init. table, answer, & offset value
    next_table = table(p)
    answer = None
    offset, next, comparisons = 0, 0, 0
    # While there is no answer, & offset does not point out of bounds
    while (answer == None) and not(offset > (len(t) - len(p))):
        comparisons += 1
        if (p[0] == t[offset]):
            # Begin iterative comparison of characters
            tslice = t[offset:]
            comparisons -= 1  # Prevents counting the first comparison twice
            trace_comps = 0
            for i,c in enumerate(p):
                # Shift i to next value
                if (i < next):
                    continue
                # Only count comparisons when i is at valid position
                trace_comps += 1
                comparisons += 1
                # If characters mismatch set new offset value & skip to next
                if (c != tslice[i]):
                    # Calculate next value
                    next = next_table[i]
                    # Append result to trace line
                    if not(offset+1 > (len(t) - len(p))):
                        trace.append(f"{' ' * offset + p} Failed pos={i}, next={next},"
                                     f" comps={trace_comps}")
                    else:
                        trace.append(f"{' ' * offset + p} Failed pos={i}, comps={trace_comps}")
                    # Calculate offset or shift
                    offset += i - next_table[i]
                    # Append the number of comparisons occurred
                    trace_comps_arr.append(str(trace_comps))
                    break
                # If on last character of p and equal then answer was found
                elif (i == len(p) - 1) and (c == tslice[i]):
                    # Append found result
                    trace.append(f"{' ' * offset + p} Found comps={trace_comps}")
                    # Append the number of comparisons
                    trace_comps_arr.append(str(trace_comps))
                    # Set answer
                    answer = offset
        else:
            # Append not found result to Trace block
            if not(offset + 1 > (len(t) - len(p))):
                trace.append(f"{' ' * offset + p + ' Failed pos=0, next=-1, comps=1'}")
                trace_comps_arr.append("1")
            else:
                trace.append(f"{' ' * offset + p + ' Failed pos=0, comps=1'}")
                trace_comps_arr.append("1")
            offset += 1
    # If no answer was found
    if (answer == None):
        trace.append("Pattern not found")
        answer = -1
    # Debug
    if (debug):
        print(f"Find: '{p}' Within: '{t}'")
        print(f"Answer = {answer}, Comparisons = {comparisons}\n")
    # Append total comparisons
    trace.append(f"Total comparisons is {'+'.join(trace_comps_arr)}={comparisons}")
    trace.append(f"See Slide 132 and Tutorial 3.3.2 for help with question.")
    # Even more debug
    if (debug):
        for line in trace:
            print(line)
        print()
    return answer, comparisons, trace


def boyer_moore_synth():
    """ This only behaves to the level of detail in the lecture videos, & notes """
    pass


if __name__ == '__main__':
    table("ABCABB")
    table("ABACB")
    table("CABABB")
    table("ABAA")
    table("ACACB")

    kmp_search("00000000", "00001", debug=True)

    pass
