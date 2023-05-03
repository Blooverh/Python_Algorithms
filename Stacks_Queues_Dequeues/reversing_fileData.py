"""This code reverses the lines of a file from its original order"""
from Stacks_Queues_Dequeues import Stack
def reverse_file(filename):
    """Overwrite given file with its contents line by line reversed"""
    S= Stack()
    originalFile=open(filename)

    for line in originalFile:
        S.push(line.rstrip('\n'))

    originalFile.close()

    #Now overwrite with contents in LIFO order
    output=open(filename,'w')

    while not S.is_empty():
        output.write(S.pop()+'\n')

    output.close()
