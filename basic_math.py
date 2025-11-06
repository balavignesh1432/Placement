import math
def countDigits():
    # Minimum will be 1 digit
    count = 1

    #Until divisor becomes 0, divide by 10. Increment counter each iteration.
    n = n // 10
    while n:
        count += 1
        n = n // 10
    # return count
    # TC - logbase10 N, Space O(1)

    #Optimal - Time O(1), Space O(1) 
    #Since no. of times is logbase 10 N, that can itself be used to say the digits
    count = int(math.log10(n)) + 1

def reverseNumber(n):
    # Count digits, for finding place value in reversed, for last digits in original number
    place = int(math.log10(n))
    # Keep adding the digits to number, so start with 0
    result = 0
    while n:    # Until divisor becomes 0, extract digits
        digit = n % 10        # Extract digits
        result += (10**place * digit) # Use digit count for place value of extracted digit.
        # Or just multiply result by 10 in each step and add to digit, so place is not needed.
        # result = result * 10 + digit
        n = n // 10  
        place -= 1  # Modify place value for next digit
    return result
    # TC - O(log10 n), SC - O(1)

# Check if number is palindrome
def isPalindrome():
    if x < 0:
        return False
    reverse = 0
    original = x
    # Reverse the number
    while x:
        digit = x % 10
        reverse = reverse * 10 + digit
        x = x // 10
    # Check if reverse is equal to original
    return original == reverse
    # TC - logbase10 N, Space O(1)
    
# Finding GCD
def calcGCD(n:int, m: int) -> int:
    # Find minimum, that can be the highest divisor. And lowest will be 1
    div = min(m, n)
    gcd = 1
    while div >= 1: # Start trying number from minimum to 1, if divided then it is GCD
        if m % div == 0 and n % div == 0:
            gcd = div
            break
        div -= 1
    return gcd
    # TC = O(min(m,n)) - In worst case goes down to 1

    # Euclidean Division Method, Keep dividing with smaller, and Update larger with remainder
    # Keep repeating until one becomes 0, the other is the answer
    while m and n:
        if m < n:
            n = n % m
        else:
            m = m % n
    return m if m else n
    # TC = O (log min(m, n)) - Since repeated divisions, in log. Height depends on min of m,n.
    # SC = O (1)

# Print all Divisors
def printDivisors(n: int) -> List[int]:
    # Trying every divisor until half    
    result = []
    for i in range(1, n//2 + 1):
        if n % i == 0:
            result.append(i)
    result.append(n)
    # return result
    # TC O(N)

    # Using the fact that you only need half the divisors, other half can be obtained by dividing with input.
    # Since half point is at, when same factor * same factor = N, so until sqrt of the number.
    # After that point it is just mirror image, since product of two factors is number
    result = []
    rootN = int(math.sqrt(n))
    for i in range(1, rootN + 1): # Find divisor until root N.
        if n % i == 0:
            result.append(i)
    
    # Calculate remaining half of the divisors
    for i in range(len(result)-1, -1, -1):
        if result[i] != n//result[i]:   #To avoid adding duplicate when perfect square
            result.append(n//result[i])
    return result
    # TC - O(root N)


def checkPrime(num):
    # Like finding divisors until root N is enough
    rootN = int(math.sqrt(num))
    # To count the divisors
    count = 0
    for i in range(1, rootN + 1): 
        if num % i == 0:
            count += 1
        if count > 1:   #If more than 1 factor then not prime
            return False
    return True
    # TC - O(root N)