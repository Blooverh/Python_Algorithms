
def eager_range(up_to):
    """create a list of integers, from 0 to up_to, exclusive"""
    seq = []
    index=0
    while index < up_to:
        seq.append(index)
        index+=1
    
    return seq

print(eager_range(5))

print()
print()

def lazy_range(up_to):
    """Generator to return the sequence of integers from 0 to up_to, exclusive"""

    index=0
    while index < up_to:
        yield index 
        index +=1

print(lazy_range(5)) #<generator object lazy_range at 0x000001F29B4DD5B0> yields in memory address the object

print()
print()


def jumping_range(up_to):
    """Generator for the sequence of integers from 0 to up_to, exclusive
    
    Sending a value into the generator will shift the sequence by that amount"""

    index = 0

    while index < up_to:
        jump = yield index 

        if jump is None:
            jump =1
        
        index += jump

if __name__ == '__main__':
    iterator= jumping_range(5)
    print(next(iterator)) #0
    print(iterator.send(2)) # jumps 2 values leading to 2
    print(next(iterator)) # 3 # after 2 is 3
    print(iterator.send(-1)) # 2 #jumps one value back leading to 2 again
    
    for x in iterator:
        print(x) # 3 and 4 - iterate the rest of function which is 3 and 4 since we yield at 2

# yield from
def lazy_range(up_to):
    """Generator to return sequence of integer from 0 to up_to, exclusive
    using yield from"""

    index=0
    def gratuitous_refactor():
        nonlocal index #index not local to this function takes value from outer function ?
        while index < up_to:
            yield index
            index +=1
    
    yield from gratuitous_refactor() #yields values from the inner function

print(lazy_range(8)) #<generator object lazy_range at 0x0000021E46FDD690>

print()
print()

"""yield from also lets us chain generators together sp that values bubble up
and down the call stack without code having to do anything special"""

def bottom():
    """Returning the yield lets the value that goes up the call stack to come right back"""
    return (yield 42)

def middle():
    return (yield from bottom()) 

def top():
    return (yield from middle())

# get the generator

gen= top()
value = next(gen)
print(value)

try:
    value = gen.send(value * 2)
except StopIteration as exc:
    value = exc.value

print(value)