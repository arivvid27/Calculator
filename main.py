import math
import replit
from time import sleep
from termcolor import colored
colors = "red", "yellow", "cyan", "magenta", "green"

def clear():
    replit.clear()

while True:
	operation = input('''
~~~~~COMMANDS~~~~~
[add]
[subtract]
[multiply]
[divide]
[integer division]
[modulo]
[power of]
[square root]
[expressions]
[quit]
>>> ''')
	clear()
	if operation == 'add':
		num1_add = float(input('num1 > '))
		num2_add = float(input('num2 > '))
		answer_add = (num1_add + num2_add)
		print(colored(answer_add, 'green'))
		sleep(5)
		clear()
	elif operation == 'subtract':
		num1_subtract = float(input('num1 > '))
		num2_subtract = float(input('num2 > '))
		answer_subtract = (num1_subtract - num2_subtract)
		print(colored(answer_subtract, 'green'))
	elif operation == 'multiply':
		num1_multiply = float(input('num1 > '))
		num2_multiply = float(input('num2 > '))
		answer_multiply = (num1_multiply * num2_multiply)
		print(colored(answer_multiply, 'green'))
		sleep(5)
		clear()
	elif operation == 'divide':
		num1_divide = float(input('num1 > '))
		num2_divide = float(input('num2 > '))
		answer_divide = (num1_divide / num2_divide)
		print(colored(answer_divide, 'green'))
		sleep(5)
		clear()
	elif operation == 'modulo':
		num1_modulo = float(input('num1 > '))
		num2_modulo = float(input('num2 > '))
		answer_modulo = (num1_modulo % num2_modulo)
		print(answer_modulo)
		sleep(5)
		clear()
	elif operation == 'integer division':
		num1_int = float(input('num1 > '))
		num2_int = float(input('num2 > '))
		answer_int = (num1_int // num2_int)
		print(colored(answer_int, "green"))
		sleep(5)
		clear()
	elif operation == 'power of':
		num1_pf = float(input('num1 > '))
		num2_pf = float(input('num2 > '))
		print(colored(num1_pf ** num2_pf, "green"))
		sleep(5)
		clear()
	elif operation == 'square root':
		num_sqrt = float(input('num > '))
		print('approx.', colored(round(math.sqrt(num_sqrt), 2), "green"))
		sleep(5)
		clear()
	elif operation == 'expressions':
		exp_ops = input('''~~~OPTIONS~~~
[equality]
-----MORE TO BE ADDED-----
>>> ''')
		if exp_ops == 'equality':
			exp1 = int(input('num1 > '))
			exp2 = int(input('num2 > '))
			if exp1 == exp2:
				print(colored('True!', 'green'))
				sleep(5)
				clear()
			else:
				print(colored('False!', "red"))
				sleep(5)
				clear()
	elif operation == 'quit':
		exit(120)
	else:
		print(colored('Give valid command', 'red'))
		sleep(5)
		clear()