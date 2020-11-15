# Hashing - Linear Probe

### Synopsis
Presents the user with random hashing questions from CSC2032 tutorials 3.2.1 & 3.1.1 using a randomized Linear Probe (LP) 
object. The LP is randomized by inserting random integers. 

### How to use - Entry Point & Question 1
To run this program simply run the questions.py python file. Upon running the program you will be prompted with a 
random question. <b>Note incorrectly answering a question displays the correct answer.</b>
        
    Suppose you have an array of size 11 and have been given
    the following simple hash function
            H(k) = k mod 11
    Then draw the array that would result from adding following
    values in the order they are given using linear probing:
            1 32 2 12 26 22 11
    Note you can use a dash '-' to represent an empty array
    location.
        
    Input answer:

Simply read the question statement then input the answer in this case:

    Input answer: 22 1 2 12 26 11 - - - - 32
    Correct!
    
### Question 2

After a question has been answered the next random question will appear such as:

    Consider the hash function H(k) = k mod 11 and the following hash array
    produced using the above hash function with linear probing:
    Searching for: 4 9 2 1
         22 12 2 1 - 16 - - 52 - 10
    Write down the answers on a piece of paper in
    Jason Steggles format shown in his videos. Then
    Compare your answers to the calculated answers!
    
    Press ENTER to reveal answers!
    
After pressing the, enter, key the answers will appear.

    Search for 4
    H(4) = 4
    Search right: empty space so not found
    
    Search for 9
    H(9) = 9
    Search right: empty space so not found
    
    Search for 2
    H(2) = 2
    Search right: found at index 2
    
    Search for 1
    H(1) = 1
    Search right: 1!=12, 1!=2, found at index 3

### Question 3

Read the question statement, input a valid answer, & press enter.

    Consider the hash function H(k) = k mod 11 and the following hash array
    produced using the above hash function with linear probing:
         - - - 3 59 38 61 27 19 53 48
    Show how the key 59 will be deleted in the above array using the remove and reinsert
    approach for deletion.
    
    Enter LP values after deletion:

Inputted answer:

    Enter LP values after deletion: - - - 3 48 38 61 27 19 53 -
    Correct!
    
### Question 4

Read the question statement, input a valid answer, & press enter.

    Suppose you have an array of size 8 and have been given
    the following simple hash function
           H(k) = k mod 8
    Consider the following array produced using hashing with
    linear probing:
           - 41 50 35 36 33 - 47
    Inserting which of the following sequences of numbers in
    the order given could have produced the above array?
    1) 35 33 36 41 47 50
    2) 41 35 50 36 47 33
    3) 50 35 41 33 47 36
    4) 36 33 47 35 50 41
    5) 36 47 33 41 50 35

    Enter choice (1-5):
    
Inputted answer:

    Enter choice (1-5): 2
    Correct!

### Tests

Please see questions.py function test_deletion() doc-string for more details.

### License

See the [LICENSE.md](LICENSE.md) file for more details.

### Acknowledgements

* Creator of original questions - [Jason Steggles](https://www.ncl.ac.uk/computing/people/profile/jasonsteggles.html#background)

### Author

* Name: <b> Lee Taylor </b>