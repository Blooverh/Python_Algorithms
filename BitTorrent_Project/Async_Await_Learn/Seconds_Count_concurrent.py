import asyncio
#written in python 3.10+
async def countdown(number, n):
    while n > 0:
        print("T-minus", n, '{}'.format(number))
        await asyncio.sleep(1) #every second we wait until next coroutine runs and stops
        n-=1

loop = asyncio.get_event_loop() #create event loop to loop function iteration
# create a list of functions that will run concurrently using asyncio std library
tasks = [
    asyncio.ensure_future(countdown("A",2)),
    asyncio.ensure_future(countdown("B",3))
]

loop.run_until_complete(asyncio.gather(*tasks)) #gather the functions in list task
"""Then run the functions until every function is completely ran"""
loop.close() #close the event loop, to free memory