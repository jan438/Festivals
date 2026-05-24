import time
from reportlab.lib.pagesizes import A3, A4

m = __import__('math', globals(), locals(), fromlist=['factorial'])

maditsi_car = 111

print(f'{maditsi_car=}')

print(m.factorial(5), time.time())

key = input("Wait")
