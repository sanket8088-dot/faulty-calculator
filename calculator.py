# Exercise 2 - Faulty Calculator
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Design a calculator which will correctly solve all the problems except
# the following ones:
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Your program should take operator  and the two numbers as input from the user
# and then return the result

print("enter your 1 NO")
a=int(input())
print("enter your 2 NO")
b=int(input())
print("enter your choice ,-,+,/,*,%")
c=(input())
if  a==45 and b==3 and c=="*":
  print("555")
elif a==56 and b==9 and c=="+":
    print("77")
elif a==56 and b==6 and c=="/":
    print("4")
elif c =="*" :
    mul=a*b
    print(mul)
elif c=="+":
    plus=a+b
    print(plus)
elif c=="/":
    div=a/b
    print(div)
elif c=="-" :
    sub=a-b
    print(sub)
elif c=="%":
    mod=a%b
    print(mod)

else:
    print("error!!! enter correct choice")