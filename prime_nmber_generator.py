#It sees if the number is prime or composite.
def is_prime(num):
    if num <= 1:
        return False
 #check for factors from 2 to the square root of number
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_generator():
# prompt user for limit and generate numbers up tot hat limit
    while True:
        try:
            upper_limit_str = input("Enter an upper limit for a number greater than 1: ")
            upper_limit = int(upper_limit_str)
            if upper_limit <= 1:
                print("Please try again and enter a number greater than 1")
                continue
            break

        except ValueError:
            print("Invalid input, please enter an integer")
        
    print("Generating prime numbers up to upper_limit")
    prime_count = 0
    for num in range(2, upper_limit + 1):
        if is_prime(num):
            print(num)
            prime_count+=1
    print(f"\n found {prime_count} prime numbers.")
    print("Project complete.")


if __name__ == "__main__":
    prime_generator()
