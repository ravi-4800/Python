import asyncio
import time

async def greetings(message):
	for i in range(6):
		print(message)
		await asyncio.sleep(1)

async def main():

	start_time = time.time()

	task1 = asyncio.create_task(greetings("hello"))
	task2 = asyncio.create_task(greetings("world"))

	await task1
	await task2

	end_time = time.time()

	print('Control returned to main()')
	print(f"Total time: {end_time - start_time}")

asyncio.run(main())