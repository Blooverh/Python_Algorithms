# STACKS

> *Stack* is a collection of objects that is inserted and removed according to LIFO (last in first out) like a stack of plates. Stacks are the simplest of all data structures yet among the most used and important.

> *STACK* is an ADT (abstract data type)

> As a consequence of the LIFO protocol, a stack can be used as a general tool to reverse a data sequence.


# Queues 

> *Queues* is a collection of objects that is inserted and and removed according to FIFO (First in First out) like a DMV line.

## Using an Array Circularly
> In developing a more robust queue implementation we allow the front of the queue to drift rightward, and we allow the contents of the queue to """WRAP AROUND""" the end of an underlying array. We assume that our array has fixed length N that is greated than the actual number of elements in the queue.
>> New Elements are enqueued towards the end of the current queue, processing from the front to index N-1 and continuing at index 0 then 1 etc based on a circular motion.

> When dequeueing an element we want to advance to the front index, we then use the arythmatic f=(f+1) % N. This receives the remainder of front index + 1 diving by N, which will allow the elements to be queued in a circular motion never exhaustong the size of the Queue as long as the Queue has less elements than the length N.

## Double ended Queues (DEQUEUE) 
> Double-ended queues are queues that allow insertion of elements at the end and front of the queue as well as deletion and the front and end of the queue.
>> We can perform the same Circular concept as one a single end queue.
