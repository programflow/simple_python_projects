import operator
from art import logo


print(logo)

cont = False
death = True
while death :  
	if cont == True:
		first_num = solution
	else:
		first_num = input("What's the first number?: ")
	operation = input(
		"""
+
-
*
/
Pick an operation: """)
	second_num = input("What's the second number?: ")
	
	operater_table = {"+":operator.add,"-": operator.sub,"*": operator.mul, "/": operator.truediv}
	
	solution = operater_table[operation] (float(first_num) ,float(second_num))

	print(f"{first_num} {operation} {second_num} = {solution}")

	new_calc = input(f"Type 'y' to continue with {solution}, or type 'n'  to start a new calculation: ")
	print(new_calc)

	if new_calc.lower() == "y":
		cont = True
	else:
		cont = False


# def my_add( x ,y):
# 	z = x + y
# 	return z

# def my_sub( x, y):
# 	z = x - y
# 	return z

# def my_mult(x, y):
# 	z = x * y
# 	return z

# def my_div(x, y):
# 	z = x / y

# def check_op( op, first_n, second_n):
# 	if op == '+':
# 		my_add(first_n, second_n)
# 	elif op == '-':
# 		my_sub(first_n, second_n)
# 	elif op == '*':
# 		my_mult(first_n, second_n)
# 	elif op == '/':
# 		my_div(first_n, second_n)
# 		