import asyncio
import time

async def greetings(message):
	for i in range(6):
		print(message)
		await asyncio.sleep(1)

async def main():

	start_time = time.time()

	await greetings("hello")
	await greetings('world')

	end_time = time.time()

	print('Control returned to main()')
	print(f"Total time: {end_time - start_time}")

asyncio.run(main())