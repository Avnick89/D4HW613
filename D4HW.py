#Calculator

from os import remove


operation = input("Enter an operator(+ - * /)")
num1 = float (input("Enter first number:"))
num2 = float (input("Enter second number:"))

if operation == "+":
    result = num1 + num2
    print (result)
elif operation =="-":
    result = num1 - num2
    print (result)   
elif operation =="*":   
     result = num1 * num2 
     print (result)
elif operation =="/":   
    result = num1 / num2 
    print (result)
else:
    (f"{operation}invalid response")





#Shopping list
s_list =[]
def add_item(s_):
    L = int(input("How many items to add to list?"))
    for i in range (L):
        item = input("Enter items for list")
        s_.append(item)
       
def remove(s_):
    item = input("Enter items to remove from list")
    s_.remove(item)

# s_list = []
# for i in range (L):+

#     item = input("Enter items for list")
#     s_list.append(item)
def display(s_):
    print("Shopping list:" ,s_list)
# input("Would you like to remove or add or quit?")
# if input == remove:
#  s_list.remove 
add_item(s_list)
remove(s_list)
display(s_list)


