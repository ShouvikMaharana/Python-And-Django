#n, t -> 2,10
# n=int(input("Enter the table of"))
# t=int(input("Enter times"))

# for i in range(1,t+1):
#     print(f"{n}x{i}={n*i}")
# print()

# i=1
# while(i<=t):
#     print(f"{n}x{i}={n*i}")
#     i+=1

# n=int(input("Enter a number"))
# # for i in range(1,n+1):
# #     if(n%i==0):
# #         print(i)

# i=1
# num=2
# isP=True
# count=0
# while(i<=n):
#     if(n%i==0):
#         #print(i)
#         i+=1
#     while(num<i):
#         if(i%num==0):
#             isP=False
#         else:
#             isP=True
# if isP==True:
#     print("Prime")
# else:
#     print("Not Prime")

# n=int(input("Enter a number"))
# t=n
# rev=0
# while t>0:
#     rev=rev*10+(t%10)
#     t=t//10
# if rev==n:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

n=int(input("Enter a number "))
i=1
fac=1
while(i<=n):
    fac=fac*i
print(fac)