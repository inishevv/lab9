import logging
from random import choice

logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="a")
logging.warning("Create")

def chislo(prompt):
    while True:
        user_n = input(prompt)
        try:
            number = int(user_n)
            return number
        except ValueError:
            print("Введено не число, попробуйте снова.")
            logging.warning("Введено не число, попробуйте снова.")

print('Введите количество боченков: ')
logging.warning('Введите количество боченков: ')
n = chislo('')
logging.warning(n)

m = []
for i in range(1, n + 1):
    m.append(i)

itog = ''
while m:
    random_item = choice(m)
    m.remove(random_item)
    itog += str(random_item)
    itog += ' '
print(itog)
logging.warning(itog)
    
