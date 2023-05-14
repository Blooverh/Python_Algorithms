# Linked List 

> Relies on a more destributed representation in which a lightweight object known as a *node* is allocated for each element.
>> Each node maintains a reference to its element and one or more references to neighboring nodes in order to collectively represent the linear order of the sequence.

## Singly linked list 

> Collection of nodes that collectively form a linear sequence. Each node stores a reference to an object that is an element of the sequence, as well as a reference to the next node in the list

>NOTE: Optional[ListNode] is a type hint in Python that indicates that a function or variable can have a value of either ListNode or None. It is used to provide type information to static type checkers and linters, and can also make it easier for developers to understand the code.

> __slots__ -> is a class variable that is usually assigned a sequence of strings that are variable names used by instances

# Circular linked lists 
## Round Robin Schedulers 

> Iterated through a collection of elements in a circular fashion and "services" each element by performing a given action on it. Such a scheduler is used, to farily allocate a resource that must be shared by a collection of clients (processes). Allocates slices of CPU time to various applications running concurrently on a computer 

> We use a queue as we dequeue a resource for the process use it, when it reaches the time limit we enqueueue the resource again for later usage while other processes are dequeueing other necessary processes.