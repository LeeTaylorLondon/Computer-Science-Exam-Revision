# Insertion-Sort
### Synopsis
I am required to learn insertion sort - a worksheet of just a few questions was released - I made this program to test the exact same questions but instead with lists of randomly generated integer values.  

### How to Use - Entry Point
Simply download, fork, or copy and paste the contents of the file and run. The program is set to infinitely ask random questions.  
Note: there are three types of questions. 
#### 1) High-level trace

    >>> You should type each integer with one space inbetween and press enter 
    
    Give a high-level trace of applying insertion sort to the array given below.
    First trace : 5 2 8 4 3
    Type trace-2: 
    
    >>> An example of valid input
    
    Give a high-level trace of applying insertion sort to the array given below.
    First trace : 5 2 8 4 3
    Type trace-2: 2 5 8 4 3
    Type trace-3: 2 5 8 4 3
    Type trace-4: 2 4 5 8 3
    Type trace-5: 2 3 4 5 8
    <You scored [4/4]!>
    
#### 2) Trace-Recognition
    
    >>> Type a single integer and press enter
    
    Consider the following array traces which may or may not have been 
    produced by different sorting algorithms when applied to the array of values:
    2 1 9 5 10

    Trace [1]
    2 1 9 5 10
    1 2 9 5 10
    1 2 9 5 10
    1 2 5 9 10
    1 2 5 9 10

    Trace [2]
    2 1 9 5 10
    1 2 9 5 10
    1 2 5 9 10
    1 2 5 9 10
    1 2 5 9 10

    >>> ... (Omitted trace 3 & 4 only in README.md for better reading)

    Which trace above corresponds to insertion sort?
    Enter number of trace: 
    
#### 3) Reverse-Trace-Recognition

    >>> Type a single integer and press enter
    >>> Note: multiple arrays could be the answer simply enter one integer
    >>>       corresponding to only one of the valid arrays! :)

    Suppose after 3 outer iterations of insertion
    sort we have the following array:
    2 5 7 8 10 3 6

    Then which of the following arrays could have been the initial
    array insertion sort was applied to.

    [1] 8 7 2 5 10 3 6
    [2] 7 8 2 5 10 3 6
    [3] 8 7 2 5 10 3 6
    [4] 5 7 2 8 10 3 6
    [5] 10 7 2 5 8 3 6

    Enter the number of any correct array: 

#### 4) Explain Stability (Stored definition can be modified)

    Question: Enter a short definition for sorting stability below.
    Answer  : 
    
    >>> User should enter stored definition for stability (below)
    >>> " if an input list contains two equal elements in positions 
    >>> i and j where i < j then in the sorted list they have to 
    >>> be in positions i' and j' "
    
    Question: Enter a short definition for sorting stability below.
    Answer  : if an input list contains two equal elements in positions i and j where i < j then in the sorted list they have to be in positions i' and j'
    <Mark_C = 31/31>
    <Mark_M = 31/31>
    <Answer = If an input list contains two equal elements in positions     i and j where i < j then in the sorted list they have to be in positions     i' and j'>
    
## Acknowledgements
* [Insertion Sort Explanation](https://www.youtube.com/watch?v=JU767SDMDvA) - Pseudo Code
* [Jason Steggles](https://www.ncl.ac.uk/computing/people/profile/jasonsteggles.html#background) - Author of Questions

## Author
* Name: __Lee Taylor__
