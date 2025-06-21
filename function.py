print("1) To print the calender: ")
import calendar
yy = 2025
mm = 6
print(calendar.month(yy, mm))

print("\n2) Factors: ")
num = 5
for i in range(1, 11):
    if num%i == 0:
        print(i)

print("\n3) Convert Decimal to Binary, Ocatal and Hexadecimal: ")
dec = 123
print("Binary: ",bin(dec))
print("Octal: ",oct(dec))
print("Hexa: ",hex(dec))

print("\n4) Find ASCII Value of Character: ")
ch = "a"
print("The ASCII value of "+ ch + " is", ord(ch))

print("\n5) Find GCD Of Two numbers: ")
g1 = 72
g2 = 120
gcd = 1


for i in range(1,min(g1,g2)+1):
    if g1%i == 0 and g2%i == 0:
        gcd = i
print("GCD of", g1, "and",g2, "is",gcd)
lcm = (g1 * g2 )//gcd
print("LCM of", g1, "and",g2, "is",lcm)

print("\n6) Calculator: ")
def calculator():
    a = input("Enter the value for add 1, sub 2, mul 3, div 4: ")

    try:
        n1 = float(input("Enter the first value: "))
        n2 = float(input("Enter the second value: "))

        if a == "1":
            c = n1 + n2
            print("The sum of the values is:", c)
        elif a == "2":
            c = n1 - n2
            print("The difference of the values is:", c)
        elif a == "3":
            c = n1 * n2
            print("The product of the values is:", c)
        elif a == "4":
            if n2 != 0:
                c = n1 / n2
                print("The division of the values is:", c)
            else:
                print("Error: Division by zero is not allowed.")
        else:
            print("Enter a valid option (1 to 4).")
    except ValueError:
        print("Invalid input: Please enter numeric values.")
calculator()
