# n=int(input("Enter a number "))
# i=1
# fac=1
# while(i<=n):
#     fac=fac*i
#     i+=1
# print(f"Factorial of number {n} is {fac}")

# n=int(input("Enter a number"))
# fibo1=0
# fibo2=1
# print(fibo1)
# print(fibo2)
# i=1
# while(i<=n):
#     fibo=fibo1+fibo2
#     print(fibo)
#     fibo1=fibo2
#     fibo2=fibo
#     i+=1

# n=int(input("Enter a number"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("* ",end="")
#     print()

# n=int(input("Enter a number"))
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print("* ",end="")
#     print()

# n=int(input("Enter a number"))
# for i in range(1,n+1):
#     for j in range(i,n):
#         print(" ",end="")
#     for k in range(1,i+1):
#         print("*",end=" ")
#     print()

# n=int(input("Enter a number"))
# for i in range(n,0,-1):
#     for j in range(1,i):
#         print(" ",end=" ")
#     for k in range(n-i+1):
#         print("*",end=" ")
#     print()

# n=int(input("Enter a number"))
# for i in range(n,0,-1):
#     for j in range(1,i):
#         print(" ",end="")
#     for k in range(n-i+1):
#         if(i%2!=0):
#             print("*",end=" ")
#         else:
#             continue
#     print()

# n=int(input("Enter a number"))
# for i in range(n):
#     for j in range(i+1):
#         print(end=" ")
#     for k in range(n):
#         print("*",end=" ")
#     print()
#     n-=1

# n=int(input("Enter a number"))
# l=int(n/2)
# for i in range(1,n-l+1):
#     for j in range(i,n-l):
#         print(" ",end="")
#     for k in range(1,i+1):
#         print("*",end=" ")
#     print()

# for i in range(l,0,-1):
#     for j in range(i,l):
#         print(" ",end="")
#     for k in range(1,i+1):
#         print(" *",end="")
#     print()

# n=int(input("Enter a number: "))
# for i in range(n):
#     for j in range(n):
#         if (i==j or i+j==n-1):
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()

n=int(input("Enter a number: "))
for i in range(n):
    for j in range(n):
        if (i==j or i+j==n-1 or i==0 or j==0 or j==n-1 or i==n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()