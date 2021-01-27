operation = input('''
~~~~~COMMANDS~~~~~
[a]dd
[s]ubtract
[m]ultiply
[d]ivide
[i]nteger division
[mo]dulo
[q]uit
>>> ''')
if operation == 'a':
	num1_add = int(input('num1 > '))
	num2_add = int(input('num2 > '))
	answer_add = (num1_add + num2_add)
	print(answer_add)
elif operation == 's':
	num1_subtract = int(input('num1 > '))
	num2_subtract = int(input('num2 > '))
	answer_subtract = (num1_subtract - num2_subtract)
	print(answer_subtract)
elif operation == 'm':
	num1_multiply = int(input('num1 > '))
	num2_multiply = int(input('num2 > '))
	answer_multiply = (num1_multiply * num2_multiply)
	print(answer_multiply)
elif operation == 'd':
	num1_divide = int(input('num1 > '))
	num2_divide = int(input('num2 > '))
	answer_divide = (num1_divide / num2_divide)
	print(answer_divide)
elif operation == 'mo':
	num1_modulo = int(input('num1 > '))
	num2_modulo = int(input('num2 > '))
	answer_modulo = (num1_modulo % num2_modulo)
	print(answer_modulo)
elif operation == 'i':
	num1_int = int(input('num1 > '))
	num2_int = int(input('num2 > '))
	answer_int = (num1_int // num2_int)
	print(answer_int)
elif operation == 'q':
	exit(120)
else:
	print('Give valid command')