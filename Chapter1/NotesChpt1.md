# Set and frozeset classes in python

    -> set class represents the mathematical notion of a set, namely a collection of elements without duplicates, and without an inherent order to those elements.

    -> Major advantage of a set vs a list is that it  has highly optimized method for checking whether a specific element is contained in the set.
        This based on the data structure names Hash Table.
    
    -> Major disadvantages: 
        1. set does not maintain the elements in any particular order. 
        2. only instances of immutable types can be added to a python set.

    -> It is possible to maintain a set of tuples, but not a set of lists or a set of sets because lists and sets are mutable and tuples are not.

    -> Frozen set class is an immutable form  of the set type, so it is legal to have a set of frozen sets