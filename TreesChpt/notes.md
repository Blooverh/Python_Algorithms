# Trees 

> Trees allow for implementation a host of algorithms much faster than when using linear data structures, such as linked lists, queues, stacks etc...

> Trees also provide natural organization for data and consequently have become a widfely present structure in files systems, GUIs, databases, websites and other computer systems.

> Relationships in trees are hierarchical, with objects being above or below other objects.

> We define a tree T as a set of nodes storing elements such as the nodes have a parent-child relationship 
>> If T is non-empty, it has a special node called the root of T, that has no parent.
>> Each node v of T is different from the root and has a unique parent node w, every node with parent w is a *child* of w.

> An *EDGE* of tree T is a pair of nodes (u,v) such that u is the parent of v, or vice versa.

> A path of T is a sequence of nodes such that any 2 consecutive nodes in a sequence form an *edge*

## Ordered Trees 

> tree is ordered if there is a meaningful linear order among the children of each node.

## TREE ADT (ABSTRACT DATA TYPE)
> we defin a Tree ADT using the concept of a position as an abstraction for a node of a tree. An element is stored at each position, and positions satisfy parent-child relationships that define the TREE structure.

## Computing depth and height of a Tree 
> let p be the position of a node of tree T. The *depth* of p is the number of ancestors of p *Excluding* p itself. Example, the root of a tree T has depth 0, other wise the depth of p is 1+ the depth of the parent of p.

> Depth running time is O(depth of p + 1), where depth  of p is based of p to the root. Because the algorithms performs in contant time recursively for each ancestor of p. Thus algorithm runs in O(n) in the worst case where n is the total number of positions of T because a position of T may have depth n-1 (since root is depth level 0) if all nodes form a single branch.

> height is the number of edges to its most distant leaf node, thus if p is a leaf, height = 0 

> *depth is the number of edges back up to the root, thus root always has a depth of 0 while leaf nodes always have a height of 0! depth and height are both the root height!!*

# BINARY TREE

> Rules: 
>> every node has at most 2 children
>> each child node is labeled as being a left or right child
>> a left child precedes a right child in the order of children of a node.

## Arithmatic Binary tree example: 

> if a node is leaf then its value is a variable or a constant
> if a node is internal, then its value is defined by applying its operation to the values of the children

## relation between internal and external nodes 
> external nodes = internal nodes + 1

## Linked strucutre for binary trees 
> A natural way to realize a binary tree is to use linked structures, with a node that maintains references to the element stored at a position p and to the nodes associated with the children of parent p. Example *if p is the root of T, then parent field of p is None*

> Thus a node in a binary tree will have a parent, a left child, a right child and a value reference, we can see it in a similar way as a linked list 

## Performance of a linked Binary Tree Implementation

> len method runs in O(1) as we use an instance variable storing the number of node of T, is_empty relies on one call from len 

> accessor methods take O(1), sibling and children methods are derived from Binary Tree class on constant number of calls to these other acessors so they run on O(1)

>depth is O(depth of p +1)

>height = O(n) since leafs are place in positions with no children hence being on the last level of the tree

## Array Based representation of a binary Tree

> if p is root of T, then position of p is 0
> if p is left child of position q, then position p is 2 * q + 1
> if p is right of position q then position o is 2 * q + 2

## Binary Tree traversal algorithms 
> *preorder* -> root is visited first, then the substrees rooted at the roots children are traversed recursively. If the tree is ordered, then suubtrees are traversed according to the order of the children.

> We start at the root and mover traversly to the next node which is the ordered child of the root if binary tree is ordered.
>> Algorithm: 
    preorder( T, p):
        perform the visit action for position p
        for each child (C) in T.Children(p) do
            preorder(T, c)

> Postorder traversal => recursively traverses the subtress rooted at the children of the root first and then visits the root, thus root will be last node to be visited.
>> we start from the left most child of root and traverse the entire tree until we reach the root node.
>> Algorithm:
    postorder(T, p):
        for each child c in T.children(p) do 
            postorder(T, c) *recursively traverse the subtree rooted at c 

> Overall running of both this algorithms is O(n) meaning it increases linearly based on the number of inputs the tree contains.

> Breadth First Traversal => Non recursive process for traversing the tree, we use a QUEUE to produce a FIFO semantics for the order in which we visit the nodes. Overall running time is O(n), due to the n calls to enqueue and n calls to dequeue as we keep nodes in queue to process the visit of such trees. We start from the root then read from left to right for each level of the tree
>> Algorithm: 
    Initialize queue Q to contain the T.root()
    while Q != empty do
        p= Q.dequeue() => p is the oldest entry in the queue meaning the position of the root node at the start
        perform the visit action for position p
        for each child c in T.children(p) do
            Q.enqueue(c) -> add p's children to the end of the queue for later visits 

> Inorder traversal -> We visit a position between the recursive traversals of its left and right subtrees. We can think of it as visiting the nodes from left to right starting from the last level (depth) of the entire tree. For every position p the inorder traversal visits p after all the positions in the left subtree of the p and before all the positions in the right subtree of p.
>> Algorithm: inorder(p):

    if p has left child lc then
        inorder(lc) => recursive traverse the left sub tree of p
    
    perform the visit action for position p

    if p has a right child rc then 
        inorder(rc) => recursive traverse the right subtree of p

# Binary Search Trees
> binary tree is a tree that can be traversed with inorder traversal algorithm since we store the elements in an ordered sequence. We visit each node from left to right in the subtree since right subtree has higher values that its parents and left subtree has lower values than its parents.

> Let S be a set (set is a structure that contains all unique numbers, meaning no repeat elements). For example we can use a binary seatch tree T for a set S to find whether a given search value v is in set S by traversing a path down the tree T, starting at the root. If a value v < element(position) search continues on the left subtree, if value v > element(position) then we traverse on the right of the subtree.

> The running time of searching in a binary tree T is propotional to the height of T.

> All traversal algorithms for binary trees (preorder, postorder, breadth first and inorder) can be used to traverse a binary search tree.

## preorder traversal 
> recrusive algorithm for generating a preorder traversal, as originally described, must be parametized by a specific position within the tree that serves as the root of a subtree to traverse 