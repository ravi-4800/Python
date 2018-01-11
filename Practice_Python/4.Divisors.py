n = int(input("Enter a number: "))
a = [i for i in range(1,n+1) if n%i==0]
print("The list of Divisors of {} is {}".format(n,a))
