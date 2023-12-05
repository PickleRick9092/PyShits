# Declare a variable to get number from user

number = int(input("Enter Number that u want to see its multiplication table : "))

# Using "For Loop"

print("The Multiplication Table of :", number)
for count in range(1,11):
    print(number,"x",count,"=",number * count)

# Using "While Loop"
count = 1
print("The Multiplication Table of :", number)
while count <= 10:
    print(number,"x",count,"=",number * count)
    count += 1