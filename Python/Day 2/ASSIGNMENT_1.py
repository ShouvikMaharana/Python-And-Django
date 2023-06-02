# n=int(input("Enter a number"))
# def fact(n):
#     i=1
#     fac=1
#     while(i<=n):
#         fac=fac*i
#         i+=1
#     return fac
# def print_fact(n):
#     print(f"Factorial of number {n} is {fact(n)}")

# print_fact(n)

n=int(input("Enter a number"))
def fibo(n):
    fibo1=0
    fibo2=1
    print(fibo1)
    print(fibo2)
    i=1
    while(i<=n):
        fibo=fibo1+fibo2
        fibo1=fibo2
        fibo2=fibo
        i+=1
        print(fibo)
        
# def print_fibo(n):
#     print(fibo(n))

fibo(n)