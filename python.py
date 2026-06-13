# a=float(input("enter a number:"))
# b=float(input("enter a number:"))
# c=float(input("enter a number:"))
# d=float(input("enter a number:"))
# if a>b and a>c and a>d:
#    print("the largest number is:",a)
# elif b>a and b>c and b>d:
#    print("the largest number is:",b)
# elif c>a and c>b and c>d:
#    print("the largest number is:",c)
# elif d>a and d>b and d>c:
#    print("the largest number is:",d
# else:
#    print("all are equal")


# name=input("name:")
# a=float(input("enter the python mark:"))
# b=float(input("enter the physics mark:"))
# c=float(input("enter the maths mark:"))
# total=a+b+c
# percentage=total/300*100
# print("total=",total)
# print("percentage=",percentage)
# if percentage>=45:
#     print(name,"is passed")
# elif percentage>=0 and percentage<45:
#     print(name,"is failed")
# else:
#     print("invalid")

# for i in range(2,101):
#     if i % 2 == 0:
#         print(i)
    

# i=1
# while i<=10:
#     if i % 2 == 0:
#         print(i)
#     i+=1        

   
# def add(a,b):
#     return a+b
# x=add(4,6)
# print(x)


# c=float(input("enter temperature in celsius:"))
# fahrenheit=(c*9/5)+32
# print("fahrenheit:",fahrenheit)


# r=100
# l=[]
# sum=0
# for num in range(1,101):
#     c=0
#     for factor in range(1,num+1):
#         if num % factor == 0:
#             c=c+1
#     if c==2:
#         l.append(num)
#         sum=sum+num
# print("list of prime",l)
# print("sum of prime:",sum)


# x=lambda a,b: a+b
# print(x(4,6))

# x=lambda a: a**0.5
# print(x(5))

x=lambda a: "even" if a % 2 == 0 else"odd"
print(x(3))