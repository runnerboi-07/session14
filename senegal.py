hello = "hello"

def greet():
    print("hello from Senegal")

def cook():
    print("We are making jollof rice")

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    print("prime numbers test")
    print(is_prime(7))
    print(is_prime(37))
    print(is_prime(101))

    print("not prime numbers test")
    print(is_prime(6))
    print(is_prime(25))
    print(is_prime(201))