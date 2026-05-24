import time
from reportlab.lib.pagesizes import A3, A4

m = __import__('math', globals(), locals(), fromlist=['factorial'])

print(m.factorial(5), time.time())

key = input("Wait")
