from datetime import datetime
name = input("Give me your name:")
age = int(input("Enter your age:"))
now = datetime.now()
print("Mr. {}, you will be of 100 years in {}".format(name,now.year+100-age))
