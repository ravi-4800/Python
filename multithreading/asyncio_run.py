import asyncio
import time

async def greetings(message):
	for i in range(6):
		print(message)
		await asyncio.sleep(1)

start_time = time.time()

asyncio.run(greetings("hello"))
asyncio.run(greetings("world"))

end_time = time.time()

print(f"Total time: {end_time - start_time}")