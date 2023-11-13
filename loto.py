import logging

logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="a")
logging.warning("Create")

def chislo(prompt):
    while True:
        user_n = input(prompt)
        try:
            number = float(user_n)
            return number
        except ValueError:
            logging.warning("Введено не число, попробуйте снова.")


logging.warning('Введите количество боченков: ')
n = chislo('')