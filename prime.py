#globalNumber = 0
def checkPrime(num): 
    if (num == 1): return False
    isPrime = True
    try:
        globalNumber = num
        while (num > 0):
            remainder = globalNumber % num
            if (remainder == 0 and num != globalNumber and  num != 1): isPrime = False
            num = num - 1
        return isPrime
    except:
        print("Error")


Max = int(input("Type a number for search primes:"))
for i in range(1,Max+1):
    print(f"Number {i}, IsPrime:{checkPrime(i)}")
