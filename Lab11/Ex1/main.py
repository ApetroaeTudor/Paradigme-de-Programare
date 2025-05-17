

import asyncio,time
my_lock = asyncio.Lock()

numbers_queue = [2,4,1,12]
queue_len = 4

async def do_sum(x):
    
    
    async with my_lock:
        num = numbers_queue.pop(0)
    sum = 0
    await asyncio.sleep(2)
    print("workernr:"+str(x) + " "+str(num/10))
    for x in range(num+1):
        sum+=x
    print(sum)
    
async def main_run_method():
    await asyncio.gather(
        *(do_sum(x) for x in range(queue_len))
    )

if __name__ == "__main__":
    
    time_start = time.monotonic()
    asyncio.run(main_run_method())
    time_end = time.monotonic() - time_start
    
    print(time_end)