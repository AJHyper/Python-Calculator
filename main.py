num1 = input ('Enter your first number: ')
num2 = input ('Enter your second number: ')
op = input ('Enter your operator: ')
if op == '+':
    print (int(num1)+ int(num2))
elif op == '-':
    print (int(num1)- int(num2))
elif op == '*':
    print (int(num1)* int(num2))
else:  
    print (int(num1)/ int(num2))
