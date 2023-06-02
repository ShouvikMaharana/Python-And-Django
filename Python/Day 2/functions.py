# def message(name,age,uni):
#     return f"My name is {name}, age {age} and university {uni}."
# data={"name":"Shouvik",
#       "age":20,
#       "uni":"SIT"}
# print(message(**data))

# n=int(input("Enter a number: "))
# def find_size(n):
#     count=0
#     while(n!=0):
#         n=n//10
#         count+=1
#     return count

# def is_armstrong(n):
#     size=find_size(n)
#     sum=0
#     temp=n
#     while(n!=0):
#         sum +=(n%10)**size
#         n=n//10
#     if sum==temp:
#         return True
#     else:
#         return False

# def armstrong_in_range(n):
#     for i in range(1, n+1):
#         if is_armstrong(i):
#             print (f"{i} is an armstrong number")
#         else:
#             print (f"{i} is not an armstrong number")

# armstrong_in_range(n)

# n=int(input("Enter a number :"))
def is_prime(n):
    for i in range(2,n//2):
        if(n==1 or n==4):
            return False
        if(n==2 or n==3):
            return True
        if(n%i!=0):
            return True
        else:
            return False
# def print_prime(n):
#     if is_prime(n):
#         print(f"{n} is not prime")
#     else:
#         print(f"{n} is prime")

# print_prime(n)


# is_prime(n)

n=int(input("Enter a number: "))
def prime_factors(n):
    for j in range(2,n+1):
        if(n%j==0):
            if(is_prime(j)):
                print(j,end=" ")
prime_factors(n)


