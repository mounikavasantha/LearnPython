a = 2 +2
print(a)
b = 2 +3 * 6
print(b)
print(48565878 * 578453)
print((5 - 1) * ((7 + 1) / (3 - 1)))
print(2 ** 8)
print(23/7)
print( 23 % 7)
print("hello"+"world")
print("hello"*5)

spam = 40
eggs = 2
spam = spam+eggs
print(spam)
spam = int(80)
print(spam)
print(float('99.99'))
int(3.3)
print(3.3+1)





# Calculate the multiplication and sum of two numbers
def fun_1(a,b):
    sum = a+b
    multiplication = a*b
    print("Sum of two numbers is:",sum)
    print("Multiplication of two numbers is:",multiplication)
# a = int(input("Enter a number:"))
# b = int(input("Enter a number:"))
# fun_1(a,b)



# Print the Sum of a Current Number and a Previous number
def fun_2():
    print("Printing current and previous number sum in a range(10)")

    for i in range(1,11):
        current_num = i
        previous_num = i-1
        sum = current_num + previous_num
        print(f"Current Number {current_num} Previous Number  {previous_num} and the Sum is : {sum}")
# fun_2()



# Write a Python code to accept a string from the user and display characters present at an even index number.

# For example, str = "PYnative". so your code should display ‘P’, ‘n’, ‘t’, ‘v’.

def fun_3(text):
    x = list(text)
    for i in x[0::2]:
        print(i)
# text = str(input("Enter a string:"))
# fun_3("PYnative")



# Write a Python code to remove characters from a string from 0 to n and return a new string.
def fun_4(text,n):
    m = text[n:]
    return m
# print(fun_4("PYnative",2))



# Write a code to return True if the list’s first and last numbers are the same. If the numbers are different, return False.
def fun_5(numbers_x):

    if numbers_x[0] == numbers_x[-1]:
        return True
    else:
        return False
numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]
# print(fun_5(numbers_y))



def first_last_same(numberList):
    # print("Given list:", numberList)

    first_num = numberList[0]
    last_num = numberList[-1]

    if first_num == last_num:
        return True
    else:
        return False

numbers_x = [10, 20, 30, 40, 10]
# print("result is", first_last_same(numbers_x))

numbers_y = [75, 65, 35, 75, 30]
# print("result is", first_last_same(numbers_y))



# Write a Python code to display numbers from a list divisible by 5

def num(list_num):
    for i in list_num:
        if i%5 == 0:
            print(i)
n =  [10, 20, 33, 46, 55]
print(num(n))

def fun_6(age):
    if age <=18:
        print("Minor")
    else:
        print("Adult")
# age = int(input("Enter your age:"))
# fun_6(age)

# # password = str(input("Enter the password: "))
# if password == "P@ssword":
#     print("welcome")
# else:
#     print("check the password")


# Write a Python code to display the current date and time.
import datetime
time = datetime.datetime.now()
print(time)