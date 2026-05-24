import time
m = __import__('math', globals(), locals(), fromlist=['factorial'])

print(m.factorial(5), time.time())

key = input("Wait")
