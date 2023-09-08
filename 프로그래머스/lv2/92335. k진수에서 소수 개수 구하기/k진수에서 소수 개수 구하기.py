import math

def is_prime(n):
    sqt = math.floor(math.sqrt(n))
    # print(f'n = {n}, sqrt = {sqt}')
    if n <= 1:
        return False

    for i in range(2, sqt+1):
        # print(f'sqrt={sqt}, i ={i}')
        if n % i == 0:
            return False
    return True

def chagne_n_binary(n, j):
    result = []
    
    decimal = n
    while decimal > 0:
        decimal, remain = divmod(decimal, j)
        result.append(str(remain))
    
    return ''.join(result[::-1])
    

def solution(n, k):
    
    changed_list = list(map(int, filter(lambda x: len(x) > 0, chagne_n_binary(n, k).split('0'))))
    
    ans = 0
    for x in changed_list:
        if is_prime(x):
            # print(f'{x} is prime')
            ans += 1
            
    return ans