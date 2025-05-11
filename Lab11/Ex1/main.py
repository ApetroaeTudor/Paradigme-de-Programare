

import asyncio
my_lock = asyncio.Lock()

numbers_queue = [2,4,1,12]
queue_len = 4

async def do_sum():
    async with my_lock:
        num = numbers_queue.pop(0)
    sum = 0
    for x in range(num+1):
        sum+=x
    print(sum)
    
async def main_run_method():
    await asyncio.gather(
        *(do_sum() for x in range(queue_len))
    )

if __name__ == "__main__":
    asyncio.run(main_run_method())