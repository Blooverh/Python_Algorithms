# RECURSION 

## Recursion
    >  - technique by which a function makes one or more calls to itself during execution
    > - or by which a data structure relies upon smaller instances of the very same type of structure in its representation. 

## Recursion Trace 
> In Python, each time a function (recursive or not) is called, a structure known as *activation record or frame* is created to store information about the progress of that invocation of the function.
    > - This activation record includes a name space for storing the function's call parameters and local variables, and information about which command in the body of the function is currently executing.
    >> When the exection of a function leads to a nested function call (recursion) the execution of the former call is suspended and its activation record stores the place in the source code at which the flow control should continue upon return of the nested call.

## File system for a computer:
> has a recursive structure in which directories can be nested arbitrarly deeply within other directories.
> Recursive algorithms are widely used to explore and manage this file systems.
    
>  Modern OS define file-system directories in a recursive way. A file systems consists of a top-level directory (example: "root directory") and the contents of this directory consist of files and other directories, which in turn can contain files and other directories.

> Many common behaviors of an OS such as copying a directory or deleting a directory, are implemented using recursive algorithms.

> ### Python OS module
    >* *os module* -> provides robust tools for interacting with the operating system during execution of a program.
>> os.path.getsize(path) - return imemediate disk usage (measure in bytes) for the file or directory that is identified by the string *path* (eg. /user/rt/courses). 

>> os.path.isdir(path) - return True if entry designated by string path is a directory; False otherwise.

>> os.listdir(path) -Return a list of strings that are names of all entries within a directory designated by string *path*

>> os.path.join(path, filename) - Compose a path string name and filename string using an appropriate operating system separator between the two ("/" or "\\\"). Returning the string that represents the full path to the file.

> Linear recursion - if a recursive function is designed so that each invocation of the body makes at most one new recursive call, this is known as linear recursion.

> Multiple Recursion - process in which a function may take more than 2 recursive calls.

### Defining Recursive Algorithms 

>Test for base cases - there should be at least 1 base case. These base cases should be defined so that every possible chain of recursive calls will eventually reach a base case, and the handling of each base case.

>Recur - If not a base case, we perform one or more recursive calls. This recursive step may involve a test that decides which of several possible  recursive calls to make. We should define each possible recursive call so that it makes progress torwards a base case.

#### Parameterizing a recursion
> To design a good algorithm, it is useful to think of the different ways we might define the subproblems that have the same general structure as the original problem.

>Tail recursion - if any recursive call that is made from one context is the very last operation in that context, with the return value of the recursive call immediately returned by enclosing recursion.

# Array-Base Sequences
> list, tuple and str classes have in common the support of indexing to access individual elements of a sequence, and each uses a low-level concept known as an array to represent that sequence.

>Encapsulation > privating the internal details of the class from outside user's who do not need to know how the class is implemented.

> * *Shallow copy* - an array copy of another array that references the same elements as in the first list.
> * With Immutable elements, shallow copies are moot.

> * *deep copy* - a copy of the original list but all elements have a different reference.

> This can be done from the copy module using the deepcopy() function.

> To produce an array of 8 elements with a value 0 we can do: counters= [0] *8, meaning all the cells in the list reference to the same object "0"

>Strings are represented as an array of characters and not an array of references. -> This is called a *Compact Array*, because the array is storing the bits that represent each character in the case of strings.
>> Advantages:
- overall memory usage will be much lower for a compact structure because there is no overhead (extra memory assigned just in case) devoted to the explicit storage of the sequence of memory references. 
- A referential strucutre will tipically use 64-bits for the memory address stored in the array, on top of whatever number of bits are used to represent the object that is considered the element.
- Also, each UNICODE character stored in a compact array within a string tipically requires 2 bytes. If each character were stored independentely as one-character string, there would be significantly more memory (bytes) used.

>How to declare an array in Python using Array module 
- primes= array('i',[2,3,4,5,6,7,8]) --- *i* > is a type code that designates the array as an array of signed integers, typically represented using at least 16-bits each integer.
- The *typecode* allows the interpreter to determine precisely how many bits are needed per element of the array.
- *Array module does not provide support for making compact arrays of user-defined data types*  
-- Example: stacks, queues, trees, linked lists, graphs, Hashmaps etc... This are not built in python data types.
> DATA TYPE Table in the book on page 191 

>The array module does not provide support for making compact arrays of user-defined data types. Compact arrays of such structures can be created with the lower-level support of a module named ctypes.

### Dynamic Arrays and Amortization 
>  When creating a low-level array in a computer system, the precise size of that array must be explicitly declared in order for the System to properly allocate a consecutive piece of memory for its storage.

> Because the system might dedicate neighboring memory locations to store other data, the capacity of an array cannot trivially be increased by expanding into subsequent cells. In Python tuple and str instances, this constraint is not a problem. The instances of these classes (tuple and str) are immutable (not possible to modify), so the correct size for an underlying array can be fixed when the object is instantiated.

> *Python's list class* presents a more insteresting abstractions. Although a list has a particular length when constructed, the class allows us to add elements to the list, with no apparent limit on the overall capacity of the list. To provide this abstraction, Python relies on *dynamic array* algorithm. 

> Because a list is a referential structure, the result of getsizeof function for a list instance only includes the size for representing its primary structure; does not account for memory used by the objects that are elements of the list. Meaning each object at ith position in the array has its own memory size along with the memory size of its reference in the array.

#### Implementing a dynamic array
>  The key is to provide means to grow the Array A that stores all the elements of a list. When an array is full and we append an element to the list we have to create a new array and copy the elements of previous array to the new array
>> A common used rule is for the new array to have twice the capacity of the existing array.

### Amortize Analysis of dynamic arrays

> Amortization -> we can show that performing a sequence of such append operations on a dynamic array is actually efficient. To perform an *amortized analysis* we use an accounting technique where we view the computer as a coin operated appliance that requires the payment of 1 cyber-dollar for a constant amount of computing time. 

> Using a *fixed* increment for each resize of the array, and thus an arithmatic progression of intermidiate array sizes, results in an overall time that is quadratic in the number of operations.

### Memory Usage and Shrinking the an array

> Another consequence of the rule of a geometric increase in capacity when appending to a dynamic array is that the final array size is guranteed to be proportional to the overall number of elements. That is, the data structure uses O(n) memory which is very desirable property for a data structure.

## Efficiency of Python's Sequence types 
### Python's List and Tuple class

> *Nonmuttating* behaviors of the list class are precisely those that are supported by the tuple class, since tuples are immutable (non changeable)

> Tuples are more memory efficient than lists because they are immutable; thus, there is no need for an underlying dynamic array with surplus capacity.

### Lexicographic Comparisons 

> Comparisons between 2 sequences are defined lexicographically.

> In worst case, evaluating such a condition requires an iteration taking time proportional to the length of the shorter of the 2 arrays, because when 1 sequences ends, the lexicographic result can be determined 
>> Example: [7,3,...] < [7,5,...] This returns true because the second element of the second array is bigger than the second elements of the first array; Therefore not needing to go through the rest of the list

### Removing elements from a list 

> list class offers several ways to remove an element from a list:
>> pop() removes the last element from a list. This is most efficient because all other elements remain in their original location. This is efficiently an O(1) operation, but the bound is amortized because Python will occasionally shrink the underlying dynamic array to conserve memory.

>> pop(k) removes the element k that is at index k < n of a list (k index). Shifting all remaining elements after to the left to fill the gap that resulted from the pop of the element at position k. Efficiency of this operation is O(n-k) still constant.  The most expensive call using pop() would be pop(0) since we have to shift every element in the list to the left to fill in the gaps from the removal of the 0 index.

>> remove() -> which removes the specified value that should be removed rather than pop() which removes the element at index k by using the index instead of the value.

### Extending a list

> Python provides a method called extend() that is used tp add all elements of 1 list to the end of a 2nd list. 

### Constructing New Lists 

> *list comprehension* example: squares=[k*k for k in range(1, n+1)] which is the same as:

    squares=[]
    for k in range(1, n+1):
        squares.append(k*k)

## Python's String class 

> The analysis for many behaviors is quite intuitive. Methods that produce a new string require time that is linear in the length of the string that is produced, since a string is an array of characters.

> Many of the behaviours that test boolean conditions of a string take O(n) time, examining all n characters in the worst case, but short circuiting as soon as the answer becomes evident. Such as checking if string is lower character and the first character is upper cased which gives automatically the reuslt False.

### Insertion Sort
> Explanation: Starting with the first element in the array, because one element by itself is already sorted we go to the next element. If the second element is smaller than the first one we swap both elements in the array. Next we consider a third element, we swap it leftwards by comparison with the previous elements until the 3rd element is in the correct position. Then we do the same for the next ones.
>Example
    Input: An array A of n comparable elements 
    Output: The array A with elements rearranged in nondecreasing order (ascending order)

    for k from 1 to n-1 do
        Insert A[k] at its proper location within A[0], A[1],..., A[k]

### Using Characters as Array Indices

> Example A=0, B=1 etc.. So When writing a Ceaser Cipher Algorithm, we apply the rotation of r as a simple formula. Replace each letter i with the letter (i+r) mode 26 which returns the remainder after performing an integer division.

> In Python characters are represented in UNICODE by integer code points, and the code points for the uppercase letters are consecutive, thus for simplicity we restrict the encryption to used only uppercase letters.

> Function to retrive the UNICODE Integer value in python is *ord(c)* which takes a parameter character c and returns the integer value associated with it.

>Function to retrive a one character string from a UNICODE integer is *chr(j)* where j is an integer value that will return the one character string.

### Multi dimensional data sets

> 2-D arrays can be also called matrices.

> *A common representation for a 2-D list in Python is a list of lists*
>> Example: data=[[22,18,709,5,33], [45,32,830,120,750], [4,880,45,66,61]] which is a matrix of 3 x 4 3 rows, and 4 columns. Meaning data[1][3] is the number 