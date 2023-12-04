#declare num variable for all 3 Way
num = int(input("Enter Number"))

#Way 1
#Regular Way 


factorial  = 1
if num < 0:
    print("Factorial For Negative Number? R u moron?")
elif num == 0:
    print(factorial)
else:
    for i in range(1,num+1):
        factorial = factorial*i
    print("(fuck)torail of",num,"is :" ,factorial )

#Way 2
# using Recursion  
def fact(n):  
    return 1 if (n==1 or n==0) else n * fact(n - 1);  
  
fact(num) 
print("Factorial of",num,"is",fact(num))  


#Way 3 
# using math-Module and factorial built-in function
import math
def fact(n):
    return (math.factorial(n))

#num = int(input("Enter Number :"))
f = fact(num)
print("Factorial of",num,"is",f)