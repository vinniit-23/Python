"""Problem: Check if a number is prime."""
print("enter number to check weather it is prime or not")
input_num = int(input())
is_prime = True
if input_num > 1:
    for i in range(1,input_num-1):
        if input_num % i == 0 :
            is_prime=False
            break
    if is_prime:
        print("Given number is prime")
    else:
        print("Given number is not a prime number")
else:
    print("Invalid input - number must be greater than 1")
   
         