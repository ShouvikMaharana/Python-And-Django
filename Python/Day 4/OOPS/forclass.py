class for_class:
    def for_loop(self,num):
        for i in range(1,num+1):
            print(i,end=" ")
        print()
    
    def for_loop_reverse(self,num):
        for i in range(num,0,-1):
            print(i,end=" ")
        print()
    
    def for_tables(self,num,t):
        for i in range(1,t+1):
            print(f"{num}x{i}={num*i}")
        print()
    
    def for_factors(self,num):
        for i in range(1,num+1):
            if(num%i==0):
                print(i)
    
    def for_prime(self,num):
        count=0
        for i in range(1,num+1):
            if(num%i==0):
                count+=1
        if(count>2):
            print(f"{num} is not prime")
        else:
            print(f"{num} is prime")

    def for_palindrome(self,num):
        t=num
        rev=0
        for i in str(num):
            rev=rev*10+(t%10)
            t=t//10 
        if rev==num:
            print(f"{num} is Palindrome")
        else:
            print(f"{num} is not Palindrome")

    def for_prime_factors(self,num):
        for i in range(1,num+1):
            if(num%i==0):
                count=0
                for j in range(1,i+1):
                    if(i%j==0):
                        count+=1
                if(count>2):
                    continue
                else:
                    print(f"{i}")
        
    def for_no_of_digits(self,num):
        count=0
        for i in str(num):
            num=num//10
            count+=1
        print(count)

    def for_armstrong(self,num):
        count=0
        temp=num
        t=num
        for i in str(num):
            num=num//10
            count+=1
        size=count
        sum=0
        for i in range(t):
            sum +=(t%10)**size
            t=t//10
        if sum==temp:
            print(f"{temp} is Armstrong")
        else:
            print(f"{temp} is not Armstrong")

                

for_obj=for_class()
for_obj.for_loop(5)
for_obj.for_loop_reverse(5)
for_obj.for_tables(5,10)
for_obj.for_factors(25)
for_obj.for_prime(7)
for_obj.for_palindrome(12321)
for_obj.for_prime_factors(40)
for_obj.for_no_of_digits(124639875)
for_obj.for_armstrong(154)
