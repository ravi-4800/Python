import asyncio
import time

async def greetings(message):
	for i in range(6):
		print(message)
		await asyncio.sleep(1)

async def print_numbers(num):
	for i in range(num):
		print(i)
		await asyncio.sleep(1)

async def main():

	start_time = time.time()

	await asyncio.gather(greetings('Hello'),
						 greetings("World"),
						 print_numbers(6))

	end_time = time.time()

	print('Control returned to main()')
	print(f"Total time: {end_time - start_time}")

asyncio.run(main())

# from telnetlib import Telnet

# def verify_email(email):
# 	to_email = email
# 	tn = Telnet('gmail-smtp-in.l.google.com', 25)
# 	tn.write(b'HELO gmail.com\n')
# 	tn.write(b'mail from:<prince14801@gmail.com>\n')
# 	tn.write(b'rcpt to'+b'<'+to_email.encode('ascii')+b'>'+b'\n')
# 	tn.write(b'QUIT\n')
# 	print(tn.read_all().decode('ascii'))

# verify_email('akdfa@gmail.com')