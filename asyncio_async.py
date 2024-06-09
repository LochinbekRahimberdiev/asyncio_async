import asyncio
import time
from datetime import datetime
from time import sleep, time
import threading
# Tasklar ro'yxati
async def asyncio_task(id):
    print(f"Task {id} started at {datetime.now().time()}")
    await asyncio.sleep(1)
    print(f"Task {id} ended at {datetime.now().time()}")

async def main():
    tasks = []
    for i in range(8):
        tasks.append(asyncio.create_task(asyncio_task(i)))
    await asyncio.gather(*tasks)

print("Running asyncio tasks:")
start_time = time.time()
asyncio.run(main())
print(f"Asyncio tasks completed in {time.time() - start_time} seconds")



def threading_task(id):
    print(f"Threading Task {id} started at {datetime.now().time()}")
    sleep(1)
    print(f"Threading Task {id} ended at {datetime.now().time()}")

print("Running threading tasks:")
start_time = time()
threads = [threading.Thread(target=threading_task, args=(i,)) for i in range(16)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
print(f"Threading tasks completed in {time() - start_time} seconds")