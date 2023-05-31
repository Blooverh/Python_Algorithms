# Trees 

> Trees allow for implementation a host of algorithms much faster than when using linear data structures, such as linked lists, queues, stacks etc...

> Trees also provide natural organization for data and consequently have become a widfely present structure in files systems, GUIs, databases, websites and other computer systems.

> Relationships in trees are hierarchical, with objects being above or below other objects.

> We define a tree T as a set of nodes storing elements such as th nodes have a parent-child relationship 
>> If T is non-empty, it has a special node called the root of T, that has no parent.
>> Each node v of T is different from the root and has a unique parent node w, every node with parent w is a *child* of w.

> An *EDGE* of tree T is a pair of nodes (u,v) such that u is the parent of v, or vice versa.

> A path of T is a sequence of nodes such that any 2 consecutive nodes in a sequence form an *edge*

## Ordered Trees 

> tree is ordered if there is a meaningful linear order among the children of each node.

## TREE ADT (ABSTRACT DATA TYPE)
> we defin a Tree ADT using the concept of a position as an abstraction for a node of a tree. An element is stored at each position, and positions satisfy parent-child relationships that define the TREE structure.

# BINARY TREE

> Rules: 
>> every node has at most 2 children
>> each child node is labeled as being a left or right child
>> a left child precedes a right child in the order of children of a node.