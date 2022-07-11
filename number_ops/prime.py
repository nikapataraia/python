def isprime(num):
    if(num < 0): return False
    if(num == 1):return False #i searched it up and in modern math 1 is not considered as prime num, prime nums have exactly two devisors, itself and 1;
    for n in range(2,int(num**0.5)+1):
        if num%n==0:
            return False
    return True


def primeNumberGenerator(low,top):
    result = []
    for x in range(low+1,top):
        if(isprime(x)): result.append(x)
    return result