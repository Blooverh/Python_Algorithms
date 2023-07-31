import asyncio 
from random import randint

async def do_stuff(ip, port):
    print(f'About to open a connection to {ip}')

    reader, writer = await asyncio.open_connection(ip, port) 

    print(f'Connection open to {ip}')
    
    await asyncio.sleep(randint(0,5)) 

    writer.close()

    print(f'closed connection to {ip}')

if __name__ == '__main__':

    loop = asyncio.get_event_loop()

    work=[

        asyncio.ensure_future(do_stuff('8.8.8.8', '53')),
        asyncio.ensure_future(do_stuff('8.8.4.4', '53')),
    ]

    loop.run_until_complete(asyncio.gather(*work))