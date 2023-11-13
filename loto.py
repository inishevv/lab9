#для вызов библиотек
import logging
from random import choice

#для записи работы программы в log-файл
logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="a")
#для обозначения старта программы в log-файле
logging.warning('Start')

#для проверки введенного значения N на число
def chislo(prompt):
    while True:
        user_n = input(prompt)
        try:
            number = int(user_n)
            return number
        except ValueError:
            print("Введено не число, попробуйте снова.")
            logging.warning("Введено не число, попробуйте снова.")

#для ввода значения N 
print('Введите количество боченков: ')
logging.warning('Введите количество боченков: ')
n = chislo('')
logging.warning(n)

#для создания массива значений боченков - "мешок с боченками"
m = []
for i in range(1, n + 1):
    m.append(i)

itog = ''
while m:
    random_item = choice(m) #для вытаскивания рандомного боченка
    m.remove(random_item) #для удаления боченка из мешка
    itog += str(random_item) #для добавления боченка в итоговую последовательность
    itog += ' '
print('Последовательность вытягивания боченков: ' + itog)
logging.warning(itog)
    
