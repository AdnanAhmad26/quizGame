num1 = float(input ("enter your First number: "))
op =  input ("enter operator:  ")
num2 = float(input ("enter your Second number: "))

if op == "+":
    print(num1 + num2)
    num1 = float(input ("enter your First number: "))
    op =  input ("enter operator:  ")
    num2 = float(input ("enter your Second number: "))
elif op == "-":
    print (num1 - num2)
    num1 = float(input ("enter your First number: "))
    op =  input ("enter operator:  ")
    num2 = float(input ("enter your Second number: "))
elif op == "*":
    print (num1 * num2)
    num1 = float(input ("enter your First number: "))
    op =  input ("enter operator:  ")
    num2 = float(input ("enter your Second number: "))
elif op == "/":
    print (num1 / num2)
    num1 = float(input ("enter your First number: "))
    op =  input ("enter operator:  ")
    num2 = float(input ("enter your Second number: "))
else:
    print("PLease enter correct operator")
    num1 = float(input ("enter your First number: "))
    op =  input ("enter operator:  ")
    num2 = float(input ("enter your Second number: "))
    

