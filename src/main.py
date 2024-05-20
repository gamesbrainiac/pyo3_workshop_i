import time

def sieve_of_eratosthenes_python(limit):
    # Create a list that will hold the boolean value of each number being prime.
    # Initially, set all numbers to True. The list needs to be limit + 1 because we include number 0 up to 'limit'.
    primes = [True] * (limit + 1)
    
    # This will hold the primes discovered
    result = []
    
    # Start checking each number from 2 to 'limit' to see if it is prime
    for number in range(2, limit + 1):
        # If primes[number] is still True, then it is a prime number
        if primes[number]:
            # Add the prime number to the result list
            result.append(number)
            
            # Mark all multiples of 'number' starting from number^2 as False
            # number^2 is used as the starting point because all smaller multiples of number
            # would have already been marked by smaller prime factors before the current 'number'.
            for multiple in range(number * number, limit + 1, number):
                primes[multiple] = False
    
    # Return the list of primes
    return result

def benchmark(limit):

    start_python = time.time()
    python_primes = sieve_of_eratosthenes_python(limit)
    print(python_primes)
    duration_python = time.time() - start_python

    print(f"Python duration: {duration_python}s")

if __name__ == "__main__":
    print(benchmark(20))  # Example limit
