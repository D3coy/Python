import asyncio

async def main():
    task = asyncio.create_task(sub())       # start f sub() execution in the time of f main() idle (in 7th string)
    print("A")
    # await sub()                # syncronus call untill f sub() finish (x)
    await asyncio.sleep(1)      # wait for sleep-time operator execution (idle)
    print("B")
    
    task_ret = await task                  # wait for f sub() as a !planned task! executed till the end
    print(f"\nReturned from sub_task function is -> [{task_ret}]")


async def sub():
    print("1")
    await asyncio.sleep(2)      # while this idle time f main() will be executed 
    print("2")
    return "string from f sub() ..."


asyncio.run(main())