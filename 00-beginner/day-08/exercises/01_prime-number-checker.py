#Write your code below this line 👇
# Create a prime number checker
def prime_checker(number):
    for divisor in range(2, number):
        if number % divisor == 0:
            print("It's not a prime number")
            return
    print("It's a prime number")

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)



