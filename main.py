import time
import asyncio
import threading

async def timeout():
    print("1st timeout is started")
    time.sleep()
    print("1st timeout is finished")

async def timeout2():
    print("2nd timeout is started")
    time.sleep()
    print("2nd timeout is finished")

async def main():
    print("main is started")
    threading.Thread(target=timeout).start()
    threading.Thread(target=timeout2).start()
    print("main is finished")

asyncio.run(main())