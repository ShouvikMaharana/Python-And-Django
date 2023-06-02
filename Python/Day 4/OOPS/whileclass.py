class while_class:
    def while_loop(self,num):
        i=1
        while(i<=num):
            print(i,end=" ")
            i+=1
    
    def while_loop_reverse(self,num):
        i=num
        while(i>0):
            print(i,end=" ")
            i-=1
    
    def while_tables(self,num,t):
        i=1
        while(i<=t):
            print(f"{num}x{i}={num*i}")
            i+=1
    
    def while_factors(self,num):
        i=1
        while(i<=num):
            if(num%i==0):
                print(i)
            i+=1
    
    def while_prime(self,num):
        i=1
        count=0
        while(i<=num):
            if(num%i==0):
                count+=1
            i+=1
        if(count>2):
            print("Not Prime")
        else:
            print("Prime")

    def while_palindrome(self,num):
        t=num
        rev=0
        while(t>0):
            rev=rev*10+(t%10)
            t=t//10
        if rev==num:
            print(f"{num} is Palindrome")
        else:
            print(f"{num} is not Palindrome")

    def while_prime_factors(self,num):
        i=1
        while(i<=num):
            if(num%i==0):
                count=0
                j=1
                while(j<=i):
                    if(i%j==0):
                        count+=1
                    j+=1
                if(count==2):
                    print(f"{i}")
            i+=1
        
    def while_no_of_digits(self,num):
        count=0
        while(num!=0):
            num=num//10
            count+=1
        print(count)

    def while_armstrong(self,num):
        count=0
        temp=num
        t=num
        while(num!=0):
            num=num//10
            count+=1
        size=count
        sum=0
        while(t>0):
            sum +=(t%10)**size
            t=t//10
        if sum==temp:
            print(f"{temp} is Armstrong")
        else:
            print(f"{temp} is not Armstrong")

                

while_obj=while_class()
while_obj.while_loop(5)
while_obj.while_loop_reverse(5)
while_obj.while_tables(5,10)
while_obj.while_factors(25)
while_obj.while_prime(7)
while_obj.while_palindrome(12321)
while_obj.while_prime_factors(40)
while_obj.while_no_of_digits(124639875)
while_obj.while_armstrong(154)