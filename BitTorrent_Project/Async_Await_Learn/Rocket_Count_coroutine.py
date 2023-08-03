import datetime
import heapq
import types
import time

class Task:
    """
    Rrepresents how long a coroutine should wait before starting again
    
    Comparison operators are implemented for use by heapq (heap priority queue)
    2-item tuples unfortunately do not work because when the datetime.datetime instances
    are equal, comparison falls to the coroutine and the do not implement comparison methods
    triggering an exception.
    
    Think of this as being like async.Task
    """
    def __init__(self, wait_until, coro):
        self.coro= coro #coroutine instance 
        self.waiting_until = wait_until #time it has to wait until it starts the countdown

    #Check equality between the waiting times of each coroutine for them to start the countdown 
    def __eq__(self, other):
        return self.waiting_until == other.waiting_until
    
    def __lt__(self, other):
        return self.waiting_until < other.waiting_until
    
class SleepingLoop:
    """An event loop focused on delaying the execution of coroutines 
    
    think of this as being like asyncio.BaseEventLoop
    """
    def __init__(self, *coros):
        self._new= coros 
        self._waiting = [] 

    def run_until_complete(self):

        # start all coroutines 
        for coro in self._new:
            wait_for = coro.send(None)
            heapq.heappush(self._waiting, Task(wait_for, coro)) # push first coroutine with smallest delay time for countdown
        
        #keep running until there is no more work to do
        while self._waiting:
            now = datetime.datetime.now() # starts timer at 0 
            # get the coroutine with the soonest resume time in heap priority queue (least time is root of the heap)
            task= heapq.heappop(self._waiting) 
            # checks if current timer value if less than delay time 
            if now < task.waiting_until:
                #we are ahead of schedule; wait until its time to resume
                delta = task.waiting_until - now
                time.sleep(delta.total_seconds()) 
                now = datetime.datetime.now()
            
            try:
                #it's time to resume the coroutine
                wait_until =  task.coro.send(now)
                heapq.heappush(self._waiting, Task(wait_until, task.coro))
            except:
                #coroutine is done
                pass

@types.coroutine
def sleep(seconds):
    """pause a coroutine for the specified number of seconds 
    think of this as being asyncio.sleep()"""

    now= datetime.datetime.now()
    wait_until =  now + datetime.timedelta(seconds=seconds)
    # make all coroutines on the call stack pause
    #the need to use yield necessitates this to be a genetator-based and no async based coroutine
    actual = yield wait_until
    #resume the execution stack, sending back how long we actually waited 
    return actual - now

async def countdown(label, length, *, delay =0):
    """Countdown for lauch for 'length' seconds, waiting 'delay' seconds"""
    print(label, 'waiting', delay, 'seconds before starting countdown')
    delta= await sleep(delay) 
    print(label, 'starting after waiting', delta)
    while length:
        print(label, 'T-minus', length)
        waited = await sleep(1)
        length -= 1
    print(label, 'lift-off!')

def main():
    """Start the event loop, counting down 3 separate launches.

    This is what a user would typically write.
    """
    loop = SleepingLoop(countdown('A', 5), countdown('B', 3, delay=2),
                        countdown('C', 4, delay=1))
    start = datetime.datetime.now()
    loop.run_until_complete()
    print('Total elapsed time is', datetime.datetime.now() - start)


if __name__ == '__main__':
    main()